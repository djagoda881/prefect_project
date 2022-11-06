import psycopg2
from sqlalchemy import create_engine
from prefect import task, flow
from sources import ExchangeRates

@task
def ConnectDB():
    engine = create_engine('postgresql://domino:domino@localhost:5432/dbdj')
    source = ExchangeRates()
    df = source.to_df()
    df.to_sql('t_exchange_rates', engine, if_exists='append', index=False)

@flow
def ex_rates_to_postgresql():
    ConnectDB()

if __name__ == "__main__":
    ex_rates_to_postgresql()
