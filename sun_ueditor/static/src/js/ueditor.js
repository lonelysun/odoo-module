openerp.born_ueditor = function(instance) {

	var QWeb = instance.web.qweb, _t = instance.web._t, _lt = instance.web._lt;

	instance.web.form.widgets.add('ueditor',
			'openerp.born_ueditor.FieldTextUeditor');

	instance.born_ueditor.FieldTextUeditor = instance.web.form.AbstractField
			.extend(instance.web.form.ReinitializeFieldMixin, {
				template : 'FieldTextUeditor',

				display_name : _lt('Ueditor'),
				widget_class : 'oe_form_field_ueditor',
				events : {
					'change input' : 'store_dom_value'
				},

				init : function(field_manager, node) {
					console.error("init");
					this._super(field_manager, node);
					this.editorDivName = 'ueditor_' + node.attrs.name;
					this.old_value = null;
				},

				parse_value : function(val, def) {

					return instance.web.parse_value(val, this, def);
				},

				initialize_content : function() {
					console.error("initialize_content");
					if (!this.get('effective_readonly')) {
						console.debug("UE创建前销毁");
						UE.delEditor(this.editorDivName);
						console.debug("UE创建");
						UE.getEditor(this.editorDivName);
						
					} else {
						console.debug("UE销毁");

//						UE.delEditor(this.editorDivName);
					}
					this.old_value = null; // will trigger a redraw
				},

				store_dom_value : function() {
					console.info(".....store_dom_value.....");
					if (!this.get('effective_readonly')&& this.is_syntax_valid()) {
						this.internal_set_value(this.parse_value(this._get_raw_value()));
					}
				},
				commit_value : function() {
					this.store_dom_value();
					return this._super();
				},

				_get_raw_value : function() {
					if (UE.getEditor(this.editorDivName) === undefined)
						return '';
					console.debug("从UE取值保存");
					
					return UE.getEditor(this.editorDivName).getContent();
				},

				render_value : function() {
					console.error("render_value");
					var show_value = this.format_value(this.get('value'), '');
					if (!this.get("effective_readonly")) {
						console.debug("UE创建前销毁");
						UE.getEditor(this.editorDivName);
						UE.getEditor(this.editorDivName).ready(function() {
						    //this是当前创建的编辑器实例
							console.debug("从后天取值赋值给UE");

						    this.setContent(show_value);
						})
						
//						this.$editor.ready(function(){
//							this.setContent(show_value);
//						});
						this.$el.trigger('resize');
					} else {
						this.$el.find('span[class="oe_form_text_content"]')
						.html(show_value);
					}
				},
				format_value : function(val, def) {
					return instance.web.format_value(val, this, def);
				}

			});
}