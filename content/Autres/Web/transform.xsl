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
          <td>nom</td>
          <td>origine</td>
        </tr>
        <xsl:for-each select="lovecraft/creature">
          <tr>
            <td><xsl:value-of select="nom"/></td>
            <td><xsl:value-of select="origine"/></td>
            <td>
              <xsl:element name="img">
                <xsl:attribute name="src"><xsl:value-of select="image"/></xsl:attribute>
              </xsl:element>
            </td>
          </tr>
        </xsl:for-each>
      </table>
    </body>
  </html>
</xsl:template>

</xsl:stylesheet>
