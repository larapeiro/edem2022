from pyspark.sql import SparkSession

def init_spark():
    print("Creating session")
    spark = SparkSession.builder.appName("EDEM_APP").getOrCreate()
    return spark

def main():
    print("Hola")

# Esto evita que si otra clase de nuestro codigo tiene que ejecutar "main", no ejecute esta. Es una forma de "proteger" esta función aislada.
if __name__ == "__main__":
    main()


'''

Comando a ejecutar en la terminal:

docker exec End2EndEjercicio_spark-master_1 /opt/spark/bin/spark-submit --master spark://spark-master:7077 -- jars /opt/spark-apps/postgresql-42.2.22.jar -- packages org.apache.spark:spark-sql-kafka-0 -- driver-memory 1G --executor-memory 1G /opt/spark-apps/main.py
'''