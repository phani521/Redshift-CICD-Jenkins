import psycopg2
def handler(event,context):
    conn = psycopg2.connect(
        host="redshift-cluster-1.cpiazh88ds78.us-east-1.redshift.amazonaws.com",
        database="dev",
        user="awsuser",
        port=5439,
        password="Admin1234")
    cur = conn.cursor()
    print("connection succussfully established")
    cur.execute("select * from users")
    print(cur.fetchall())
    print(".........")
    print()
    conn.close()
