<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2020-03-17 09:34:40 SA"/>
        <attribute name="created" value="QWRtaW47TUFZMzE7MjAyMC0wMy0xNzswOToyMDozNiBTQTsyMDkw"/>
        <attribute name="edited" value="QWRtaW47TUFZMzE7MjAyMC0wMy0xNzswOTozNDo0MCBTQTsxOzIxOTg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="a, b, c, x1, x2, denta" type="Integer" array="False" size=""/>
            <output expression="&quot;nhap a&quot;" newline="True"/>
            <input variable="a"/>
            <output expression="&quot;nhap b&quot;" newline="True"/>
            <input variable="b"/>
            <output expression="&quot;nhap c&quot;" newline="True"/>
            <input variable="c"/>
            <assign variable="denta" expression="b^2-4*a*c"/>
            <if expression="denta&gt;=0">
                <then>
                    <assign variable="x1" expression="(-b+sqrt(denta))/(2*a)"/>
                    <assign variable="x2" expression="(-b-sqrt(denta))/(2*a)"/>
                    <output expression="&quot;x1 la: &quot;&amp;x1" newline="True"/>
                    <output expression="&quot;x2 la: &quot;&amp;x2" newline="True"/>
                </then>
                <else>
                    <output expression="&quot;pt vo nghiem&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>
