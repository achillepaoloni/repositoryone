import java.sql.*;
 import org.h2.jdbcx.JdbcConnectionPool;
 public class BorseStudioH2 {
     public static void main(String... args) throws Exception {
         JdbcConnectionPool cp = JdbcConnectionPool.create(
             "jdbc:h2:~/bds", "sa", "");
		System.out.println("PAOLONI 1");
         String sql="SELECT * FROM UTENTEPASSWORD";  
         //for (String sql : args) {
             System.out.println("PAOLONI 2");
             Connection conn = cp.getConnection();
             conn.createStatement().execute(sql);
		System.out.println("ok sql eseguito");
             conn.close();
         //}
         cp.dispose();
     }
 }
