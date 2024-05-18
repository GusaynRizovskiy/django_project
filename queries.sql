SELECT "django_migrations"."id",
       "django_migrations"."app",
       "django_migrations"."name",
       "django_migrations"."applied"
FROM "django_migrations";



SELECT "shopapp_order"."id",
       "shopapp_order"."delivery_address",
       "shopapp_order"."promocode",
       "shopapp_order"."created_at",
       "shopapp_order"."user_id",
       "shopapp_order"."rece
        ipt ", (CAST(SUM(" shopapp_product "." price ") AS NUMERIC)) AS " total ", COUNT(" shopapp_order_products "." product_id ") AS " products_count " FROM " shopapp_order " LEFT OUTER JOIN " shopapp_o
        rder_products " ON (" shopapp_order "." id " = " shopapp_order_products "." order_id ") LEFT OUTER JOIN " shopapp_product " ON (" shopapp_order_products "." product_id " = " shopapp_product "." id ")
GROUP BY "shopapp_order"."id", "shopapp_order"."delivery_address", "shopapp_order"."promocode",
         "shopapp_order"."created_at", "shopapp_order"."user_id", "shopapp_order"."receipt";


SELECT "shopapp_order"."id"
     , "shopapp_order"."delivery_address"
     , "shopapp_order"."promocode"
     , "shopapp_order"."created_at"
     , "shopapp_order"."user_id"
     , "shopapp_order"."rece
        ipt ", (CAST(COALESCE((CAST(SUM(" shopapp_product "." price ") AS NUMERIC)), (CAST('0' AS NUMERIC))) AS NUMERIC)) AS " total ", COUNT(" shopapp_order_products "." product_id ") AS " products_c
        ount " FROM " shopapp_order " LEFT OUTER JOIN " shopapp_order_products " ON (" shopapp_order "." id " = " shopapp_order_products "." order_id ") LEFT OUTER JOIN " shopapp_product " ON (" shopapp_o
        rder_products "." product_id " = " shopapp_product "." id ") GROUP BY " shopapp_order "." id ", " shopapp_order "." delivery_address ", " shopapp_order "." promocode ", " shopapp_order "." created_at ",  " shopapp_order "." user_id "
     , "shopapp_order"."receipt";

