import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-shopinvader-odoo-shopinvader",
    description="Meta package for shopinvader-odoo-shopinvader Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-base_url',
        'odoo10-addon-partner_contact_company',
        'odoo10-addon-product_online_category',
        'odoo10-addon-product_stock_state',
        'odoo10-addon-shopinvader',
        'odoo10-addon-shopinvader_algolia',
        'odoo10-addon-shopinvader_assortment',
        'odoo10-addon-shopinvader_backend_image_proxy',
        'odoo10-addon-shopinvader_cart_expiry',
        'odoo10-addon-shopinvader_contact_company',
        'odoo10-addon-shopinvader_custom_attribute',
        'odoo10-addon-shopinvader_delivery_carrier',
        'odoo10-addon-shopinvader_delivery_instruction',
        'odoo10-addon-shopinvader_demo_app',
        'odoo10-addon-shopinvader_elasticsearch',
        'odoo10-addon-shopinvader_guest_mode',
        'odoo10-addon-shopinvader_image',
        'odoo10-addon-shopinvader_import_image',
        'odoo10-addon-shopinvader_invoice',
        'odoo10-addon-shopinvader_lead',
        'odoo10-addon-shopinvader_locomotive',
        'odoo10-addon-shopinvader_locomotive_contact_company',
        'odoo10-addon-shopinvader_locomotive_guest_mode',
        'odoo10-addon-shopinvader_locomotive_reset_password',
        'odoo10-addon-shopinvader_multi_category',
        'odoo10-addon-shopinvader_partner_vat',
        'odoo10-addon-shopinvader_pending_cart_reminder',
        'odoo10-addon-shopinvader_product_media',
        'odoo10-addon-shopinvader_product_new',
        'odoo10-addon-shopinvader_product_stock',
        'odoo10-addon-shopinvader_product_stock_state',
        'odoo10-addon-shopinvader_product_template_multi_link',
        'odoo10-addon-shopinvader_product_variant_selector',
        'odoo10-addon-shopinvader_promotion_rule',
        'odoo10-addon-shopinvader_quotation',
        'odoo10-addon-shopinvader_sale_profile',
        'odoo10-addon-shopinvader_sale_report',
        'odoo10-addon-shopinvader_search_engine',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
