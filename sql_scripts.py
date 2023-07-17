
queryList = {
    'queryVtexAccounts': '''
                        SELECT 
                            CONTA, 
                            CHAVE, 
                            TOKEN 
                        FROM 
                            acessos_vtex 
                        WHERE 
                            ATIVO = 'T' '''
}
