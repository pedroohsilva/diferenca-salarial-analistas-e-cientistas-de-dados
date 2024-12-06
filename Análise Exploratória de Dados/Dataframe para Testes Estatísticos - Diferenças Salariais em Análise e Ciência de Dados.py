# Databricks notebook source
# MAGIC %md
# MAGIC ### Construindo um Dataframe para Testes Estatísticos: Diferenças Salariais em Análise e Ciência de Dados
# MAGIC
# MAGIC Para garantir uma análise mais focada e relevante, utilizei o Databricks para criar um notebook dedicado à construção de um dataframe específico. Por meio de consultas **SQL**, esse dataframe reúne informações de cargos como Analistas e Cientistas de Dados e seus respectivos salários em dólar. Essa abordagem facilita a preparação dos dados e direciona as etapas subsequentes para a realização de **testes estatísticos** com maior precisão e eficiência.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Visualizando o Conjunto de Dados:
# MAGIC
# MAGIC Selecionando as 10 primeiras linhas do dataset para uma visualização inicial dos dados.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   *
# MAGIC FROM jobs_in_data_csv
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Selecionando Dados para Análise Estatística:
# MAGIC
# MAGIC Criando um dataframe contendo apenas as colunas de cargos específicos (Analistas e Cientistas de Dados) e seus respectivos salários em dólar, como preparação para os testes estatísticos.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     job_title,
# MAGIC     salary_in_usd
# MAGIC FROM jobs_in_data_csv
# MAGIC WHERE
# MAGIC     job_title IN ('Data Analyst', 'Data Scientist')
# MAGIC GROUP BY job_title, salary_in_usd;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Conclusão:
# MAGIC
# MAGIC Com a execução da query final, obtivemos um **dataframe consolidado** com as informações necessárias para os **testes estatísticos**. Esse dataframe contém os cargos de interesse, Analistas e Cientistas de Dados, e seus respectivos salários em dólar, proporcionando uma base estruturada e confiável para avançarmos com análises direcionadas e significativas.
