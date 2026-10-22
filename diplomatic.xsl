<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="tei">
        <xsl:output method="html" encoding="utf-8"/>

        <xsl:template match="tei:p">
    <p><xsl:apply-templates/></p>
        </xsl:template>

        <xsl:template match="/">
                <html lang="fr">
                        <head>
                                <meta charset="utf-8"/>
                                <title><xsl:value-of select="//tei:titleStmt/tei:title[1]"/></title>
                                <link rel="stylesheet" href="diplomatic.css"/>
                        </head>
                        <body>
                                <xsl:apply-templates select="//tei:body"/>
                        </body>
                </html>
        </xsl:template>
<xsl:template match="tei:choice">
<xsl:apply-templates select= "tei:orig|tei:abbr|tei:sic"/>
</xsl:template>

<xsl:template match="tei:lb">
<span class="lb" data-n="{@n}"></span>
        </xsl:template>
<xsl:template match="tei:lb"><xsl:text> </xsl:text></xsl:template>
<xsl:template match="tei:lb[@break='no']"/>
</xsl:stylesheet>
