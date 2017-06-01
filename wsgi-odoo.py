import odoo
odoo.multi_process = True
odoo.conf.server_wide_modules = ['web']

conf = odoo.tools.config
conf['addons_path'] = '/home/project/odoo-10/odoo/addons'
conf['proxy_mode'] = 'True'
conf['debug_mode'] = 'False'

application = odoo.service.wsgi_server.application
odoo.service.server.load_server_wide_modules()
