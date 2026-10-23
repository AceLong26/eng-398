<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:tei="http://www.tei-c.org/ns/1.0"
  exclude-result-prefixes="tei">

  <xsl:output method="html" encoding="utf-8" indent="yes"/>

  <xsl:template match="/">
    <xsl:text disable-output-escaping="yes">&lt;!DOCTYPE html&gt;&#10;</xsl:text>
    <html lang="fr">
      <head>
        <meta charset="utf-8"/>
        <title><xsl:value-of select="//tei:titleStmt/tei:title[1]"/></title>
        <link rel="stylesheet" href="reading.css"/>
      </head>
      <body>
        <xsl:apply-templates select="//tei:text/tei:body"/>
      </body>
    </html>
  </xsl:template>

  <!-- <div> -> Display as a section using its @type -->
  <xsl:template match="tei:div">
    <section class="{@type}">
      <xsl:apply-templates/>
    </section>
  </xsl:template>

  <!-- <head> -> Display as a heading -->
  <xsl:template match="tei:head">
    <h2>
      <xsl:apply-templates/>
    </h2>
  </xsl:template>

  <!-- <p> -> Display as a paragraph -->
  <xsl:template match="tei:p">
    <p>
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <!-- <choice> -> Show <reg>, <expan>, or <corr> -->
  <xsl:template match="tei:choice">
    <xsl:apply-templates select="tei:reg | tei:expan | tei:corr"/>
  </xsl:template>

  <!-- <lb/> -> Replace with a space retaining milestone with @data-n -->
  <xsl:template match="tei:lb">
    <span class="lb" data-n="{@n}">
      <xsl:text> </xsl:text>
    </span>
  </xsl:template>

  <!-- <pb/> -> Page break milestone -->
  <xsl:template match="tei:pb"/>

</xsl:stylesheet>

