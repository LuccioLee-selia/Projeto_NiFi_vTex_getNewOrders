
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
        'timedelta' : 1
    },
    'getAllNewOrdersVtex_30DaysOxitec': {
        'sql_query': '''
                    SELECT 
                        CONTA,
                        CHAVE,
                        TOKEN 
                    FROM 
                        acessos_vtex
                    WHERE 
                        ACESSO_VTEX IN (22)''',
        'nowStrftime' : "%Y-%m-%dT23:59:59.999Z",
        'yesterdayStrftime' : "%Y-%m-%dT00:00:00.000Z",
        'timedelta' : 30
    }

}
