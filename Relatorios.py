import os
from Consultas.Consulta import Resultado_Consultas_MK
from Save_Convert.Save_to_Excel import Save_to_Excel

consulta = Resultado_Consultas_MK()
save = Save_to_Excel()

# -------------------------------------------------
print('\nBloqueio')
cidade, df_ , name_columns_cidade = consulta.bloqueios_por_cidades()
df_.to_csv('saves/csv/bloqueios_por_cidades.csv')

mes , df_, name_columns_mes = consulta.bloqueios_total_por_mes()
df_.to_csv('saves/csv/bloqueios_total_por_mes.csv')

save.Create_Cidades_e_Geral(cidade, mes, 'Bloqueio.xlsx', name_columns_cidade, 'Bloqueio')
# ------------------------------------------------- 

cidade, df_ , name_columns_cidade = consulta.evolucao_bloqueios_por_cidade()
df_.to_csv('saves/csv/evolucao_bloqueios_por_cidade.csv')

mes , df_, name_columns_mes = consulta.evolucao_bloqueios_totais_por_mes()
df_.to_csv('saves/csv/evolucao_bloqueios_totais_por_mes.csv')

save.Create_Cidades_e_Geral(cidade, mes, 'Evolucao_Bloqueio.xlsx', name_columns_cidade, 'Evolucação Bloqueio')

# -------------------------------------------------

print('\nCancelamento')
cidade, df_ , name_columns_cidade = consulta.cancelamentos_por_cidades()
df_.to_csv('saves/csv/cancelamentos_por_cidades.csv')

mes , df_, name_columns_mes = consulta.cancelamentos_geral_por_mes()
df_.to_csv('saves/csv/cancelamentos_geral_por_mes.csv')

save.Create_Cidades_e_Geral(cidade, mes, 'Cancelamento.xlsx', name_columns_cidade, 'Cancelamento')

# # -------------------------------------------------

print('\nFaturamento')
cidade, df_ , name_columns_cidade = consulta.faturamento_por_cidades()
df_.to_csv('saves/csv/faturamento_por_cidades.csv')

mes , df_, name_columns_mes = consulta.faturamento_geral_por_mes()
df_.to_csv('saves/csv/faturamento_geral_por_mes.csv')

save.Create_Cidades_e_Geral(cidade, mes, 'Faturamento.xlsx', name_columns_cidade, 'Faturamento')

# # -------------------------------------------------

print('\nVendas')
cidade, df_ , name_columns_cidade = consulta.vendas_por_cidades()
df_.to_csv('saves/csv/vendas_por_cidades.csv')

mes , df_, name_columns_mes = consulta.vendas_geral_por_mes()
df_.to_csv('saves/csv/vendas_geral_por_mes.csv')

save.Create_Cidades_e_Geral(cidade, mes, 'Vendas.xlsx', name_columns_cidade, 'Vendas')

# # -------------------------------------------------

print('\nPagamentos')
result, df_ , name_columns = consulta.pagamentos_geral()
df_.to_csv('saves/csv/pagamentos_geral.csv')

save.Create_Simple_return(result, 'Pagamentos.xlsx', name_columns_cidade, 'Pagamentos')

# # -------------------------------------------------

print('\nRecebimentos')
cidade, df_ , name_columns_cidade = consulta.recebimentos_por_cidades()
df_.to_csv('saves/csv/recebimentos_por_cidades.csv')

mes , df_, name_columns_mes = consulta.recebimentos_geral_por_mes()
df_.to_csv('saves/csv/recebimentos_geral_por_mes.csv')

save.Create_Cidades_e_Geral(cidade, mes, 'Recebimentos.xlsx', name_columns_cidade, 'Recebimentos')

# # -------------------------------------------------

print('\nSPC')
result, df_ , name_columns = consulta.evolucao_spc_cadastradas()
df_.to_csv('saves/csv/evolucao_spc_cadastradas.csv')

save.Create_Simple_return(result, 'Evolucao_Cadastro_SPC.xlsx', name_columns, 'Evolução Cadastro de faturas no SPC')

result, df_ , name_columns = consulta.evolucao_spc_retiradas()
df_.to_csv('saves/csv/evolucao_spc_retiradas.csv')

save.Create_Simple_return(result, 'Evolucao_Retiradas_SPC.xlsx', name_columns, 'Evolução Retiradas de faturas no SPC')

# # -------------------------------------------------

result, df_ , name_columns = consulta.spc_cadastradas_mensal()
df_.to_csv('saves/csv/spc_cadastradas_mensal.csv')

save.Create_Simple_return(result, 'Cadastro_SPC_Mensal.xlsx', name_columns, 'Cadastro de faturas Mensal no SPC')

result, df_ , name_columns = consulta.spc_retiradas_mensal()
df_.to_csv('saves/csv/spc_retiradas_mensal.csv')

save.Create_Simple_return(result, 'Retiradas_SPC_Mensal.xlsx', name_columns, 'Retiradas de faturas Mensal no SPC')

# -------------------------------------------------

print('\nEvolução de Base')
cidade_1, df_ , name_columns_cidade = consulta.evolucao_contratos_criados_por_cidades()
df_.to_csv('saves/csv/evolucao_contratos_criados_por_cidades.csv')

cidade, df_ , name_columns_cidade = consulta.evolucao_contratos_cancelados_por_cidades()
df_.to_csv('saves/csv/evolucao_contratos_cancelados_por_cidades.csv')

mes, df_ , name_columns_cidade = consulta.evolucao_contratos_criados_e_cancelados_totais()
df_.to_csv('saves/csv/evolucao_contratos_criados_e_cancelados_totais.csv')

save.Create_evolucao_base(cidade_1, cidade, mes, 'Evolucao_de_Base.xlsx', ['Data','Cidade', 'Contratos_Criados', 'Constratos_Cancelados', 'Contratos_Ativos'], 'Evolução de Base')

# # -------------------------------------------------

# # -------------------------------------------------

print('\nEvolução de Base Sem Migraçao')
cidade_1, df_ , name_columns_cidade = consulta.evolucao_contratos_criados_por_cidades_sem_migracao()
df_.to_csv('saves/csv/evolucao_contratos_criados_por_cidades_sem_migracao.csv')

cidade, df_ , name_columns_cidade = consulta.evolucao_contratos_cancelados_por_cidades_sem_migracao()
df_.to_csv('saves/csv/evolucao_contratos_cancelados_por_cidades_sem_migracao.csv')

mes, df_ , name_columns_cidade = consulta.evolucao_contratos_criados_e_cancelados_totais_sem_migracao()
df_.to_csv('saves/csv/evolucao_contratos_criados_e_cancelados_totais_sem_migracao.csv')

save.Create_evolucao_base(cidade_1, cidade, mes, 'Evolucao_de_Base_Sem_Migracao.xlsx', ['Data','Cidade', 'Contratos_Criados', 'Constratos_Cancelados', 'Contratos_Ativos'], 'Evolução de Base Sem Migracao')

# # -------------------------------------------------

print('\nInadimplencia')
cidade, df_ , name_columns_cidade = consulta.inadimplencia_por_cidades()
df_.to_csv('saves/csv/inadimplencia_por_cidades.csv')

mes , df_, name_columns_mes = consulta.inadimplencia_total_por_mes()
df_.to_csv('saves/csv/inadimplencia_total_por_mes.csv')

save.Create_Cidades_e_Geral(cidade, mes, 'Inadimplencia.xlsx', name_columns_cidade, 'Inadimplencia')

# # -------------------------------------------------

cidade, df_ , name_columns_cidade = consulta.evolucao_inadimplencia_por_cidade()
df_.to_csv('saves/csv/evolucao_inadimplencia_por_cidade.csv')

mes , df_, name_columns_mes = consulta.evolucao_inadimplencia_totais_por_mes()
df_.to_csv('saves/csv/evolucao_inadimplencia_totais_por_mes.csv')

save.Create_Cidades_e_Geral(cidade, mes, 'Evolucao_Inadimplencia.xlsx', name_columns_cidade, 'Evolução Inadimplencia')

# -------------------------------------------------

print('\n')
os.system('taskkill /IM "EXCEL.EXE" /F')
print('\nFINISHED!')