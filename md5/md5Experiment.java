import java.nio.charset.StandardCharsets;
import java.security.NoSuchAlgorithmException;
import java.security.MessageDigest;

import java.math.BigInteger;
 

class md5Experiment {
    public static int getDatabaseID(String domainName, int totalShards) {
        byte[] bytesOfDomainName = domainName.getBytes(StandardCharsets.UTF_8);

        try {
          MessageDigest md = MessageDigest.getInstance("MD5");
          byte[] md5Digest = md.digest(bytesOfDomainName);
          BigInteger parameterInt = new BigInteger(1, md5Digest);
          //System.out.println(parameterInt);
          BigInteger modulus = new BigInteger(Integer.toString(totalShards));
          BigInteger shard_id = parameterInt.mod(modulus);
          return shard_id.intValue();
        }
        catch (NoSuchAlgorithmException e) {
          System.err.println("I'm sorry, but MD5 is not a valid message digest algorithm. Exiting..");
          System.exit(1);
        }

        return 9999;
    }

    public static void main(String[] args) {
        System.out.println(getDatabaseID(args[0], 64));
    }
}
