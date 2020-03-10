encoding = 'UTF-8'
import cx_Oracle

def db_connection():

        #Oracle database connection
        #Replace with your user, password, ip andress, port and database used
        ora_conn = cx_Oracle.connect('user/password@ip:port/database')
        ora_cur = ora_conn.cursor()

        #version connection
        print(f'version connection: {ora_conn.version}\n')

        #open a file
        archive = open('save.txt', 'w')

        #SQL command
        sql_command = """INSERT YOUR SQL COMMAND"""

        #execute your command in database
        ora_cur.execute(sql_command)

        #search for result of command
        result = ora_cur.fetchone()

        #if don't have result
        if result == None:
                print ("Don't have data.")
        else:
                #if return result
                while result:
                        #write in file txt
                        for x in result:
                                archive.write(f'{str(x)}|')
                        archive.write('\n')
                        #print result on screen
                        print (result)
                        result = ora_cur.fetchone()

        #close connection, cursor and file
        ora_cur.close()
        ora_conn.close()
        archive.close()

if(__name__ == '__main__'):
        db_connection()
