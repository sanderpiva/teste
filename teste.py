# --- 1 Carregando Dataframe SELIC e obtendo informações sobre os dados quanto a valores missing ---
selic_file = '/content/STP-20251001161617503_selic.csv'

try:
    df_selic = pd.read_csv(selic_file, on_bad_lines='warn', sep=';')
    print(f"Dataset {df_selic} carregado com sucesso com utf-8 e separador ';'.")
except UnicodeDecodeError:
    df_selic = pd.read_csv(selic_file, encoding='latin1', on_bad_lines='warn', sep=';')
    print(f"Dataset {df_selic} carregado com sucesso com latin1 e separador ';'.")
except Exception as e:
    print(f"Erro ao carregar o dataset {df_selic}: {e}")

print(f"\nPrimeiras 5 linhas do dataset {selic_file}:")
display(df_selic.head())
print(f"\nInformações do dataset {selic_file}:")
df_selic.info()