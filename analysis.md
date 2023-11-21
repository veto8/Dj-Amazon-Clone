product:
    -name
    -sku
    -brand      *[name-img]
    -image      *
    -price
    -reviews    *[user_id-product_id-rate[0:5]      -feedback-datetime]
    -subtitle
    -description
    -tags       *package
    -flags[new-sale-feature]
    -category   *[name-img]
    -quantity

order
    -status [recived-processed-shipped-delevered]
    -user
    -id
    -total_item
    -order_time
    -delevery_time
    -sub_total
    -total

order_table
    -order_id
    -product_id
    -price
    -quantity
    -total

user
    -name
    -emial
    -image
    -phone_number *
    -address *