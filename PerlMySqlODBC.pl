#!C:\Perl\bin\perl.exe -w

use Win32::ODBC;

$db = new Win32::ODBC( "BDSMYSQL" ) || die "Error connecting: " . Win32::ODBC::Error();

print "DRIVER ODBC PER MY SQL SERVER" . "\n";

print "***************************************" . "\n";

if( ! $db->Sql( "SELECT * FROM anagrafico" ) )

{

  while( $db->FetchRow( \%Data ) )

  {

    $Row++;

    print "$Row)";

    $Nominativo = $db->Data('Nominativo');

    $DataNascita = $db->Data('DataNascita');

    $LuogoNascita = $db->Data('LuogoNascita');

    print "NOMINATIVO: " . $Nominativo . "\n";

    print "$Row)";

    print "DATA NASCITA: " . $DataNascita . "\n";

    print "$Row)";

    print "LUOGO NASCITA: " . $LuogoNascita . "\n";

    print "***************************************" . "\n";

  }

 }

 else

 {

   print "Unable to execute query: " . $db->Error() . "\n";

 }

$db->Close(); 
