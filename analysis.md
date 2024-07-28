## DB Analysis ##

    Products :

        Product:
            - name
            - sku
            - brand
            - price
            - desc
            - tags
            -- weight --
            - flag: new , Feature

        Category:
            - name
            - image

        Reviews:
            - product
            - user
            - rate
            - review
            - create_date

        Images:
            - product
            - image

        Coupons & Offers


    Users :

        Profile:
            - name
            - email
            - image

        User Phone Number:
            - user
            - phone_number
            - type

        User Address:
            - user
            - address
            - title


    Orders :
        Order:
            - id
            - order_status [Recieved - Processed - Shipped - Delivered]
            - order_time
            - delivery_time
            - sub_total
            - discount
            - delivery_fee
            - total
            - delivery_location

        Order Details:
            - serial
            - order
            - product
            - price
            - quantity
