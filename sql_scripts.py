
queryList = {
    'getAllNewOrdersVtex_Recent' : {
        'sql_query': '''
                    SELECT 
                        CONTA, 
                        CHAVE, 
                        TOKEN 
                    FROM 
                        acessos_vtex 
                    WHERE 
                        ATIVO = 'T' ''',
        'nowStrftime' : "%Y-%m-%dT%H:%M:%S.%fZ",
        'yesterdayStrftime' : "%Y-%m-%dT%H:%M:%S.%fZ",
        'timedelta' : 1,
        'resultSuccessTable' : 'temp_OrdersVtexSuccessRecent',
        'resultFailedTable' : 'temp_OrdersVtexfailureRecent'
    },
    'getAllNewOrdersVtex_30Days': {
        'sql_query': '''
                    SELECT
                        CONTA,
                        CHAVE,
                        TOKEN 
                    FROM 
                        acessos_vtex
                    WHERE 
                        ATIVO = 'T'
                    ''',
        'nowStrftime' : "%Y-%m-%dT23:59:59.999Z",
        'yesterdayStrftime' : "%Y-%m-%dT00:00:00.000Z",
        'timedelta' : 30,
        'resultSuccessTable' : 'temp_OrdersVtexSuccess30Days',
        'resultFailedTable' : 'temp_OrdersVtexfailure30Days'
    },
    'getOrders_temptables' : {
        'sql_query' : '''
                    SELECT
                        tovsr.orderId,
                        av.CHAVE,
                        av.TOKEN,
                        tovsr.hostname as CONTA
                    FROM
                        [temp_OrdersVtexSuccessRecent] tovsr
                    LEFT JOIN
                        acessos_vtex av ON tovsr.hostname = av.CONTA
                    WHERE
                        tovsr.hostname <> 'distribuidor'
                    ''',
        'sql_querySequence' : '''
                    SELECT
                        NEXT VALUE FOR dbo.SEQ_ID_PEDIDO_VTEX as ID_PEDIDO
                    '''
    },
    'getOrders_pedidosVtex' : {
        'sql_query' : '''
                    SELECT 
                        pvtex.ID_PEDIDO_VTEX,
                        pvtex.orderId, 
                        avtex.CONTA,
                        avtex.CHAVE, 
                        avtex.TOKEN
                    FROM pedidos_vtex pvtex
                    INNER JOIN acessos_vtex avtex ON avtex.CONTA = pvtex.accountHostname
                    WHERE status NOT IN ('invoiced','replaced','canceled')
                    AND avtex.ATIVO = 'T'
                    '''
    }
}
