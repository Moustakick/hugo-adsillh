<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html lang="en" dir="ltr">
    <head>
      <title>LOVECRAFT</title>
    </head>
    <body>
      <table border="1">
        <tr>
          <th>Appellation</th>
          <th>Chateau</th>
          <th>Année</th>
        </tr>
        <xsl:for-each select="cave/bouteille">
          <tr>
            <td><xsl:value-of select="appellation"/></td>
            <td><xsl:value-of select="chateau"/></td>
            <td><xsl:value-of select="annee"/></td>
          </tr>
        </xsl:for-each>
      </table>
    </body>
  </html>
</xsl:template>

</xsl:stylesheet>
