<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Dell"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2020-02-28 04:59:06 PM"/>
        <attribute name="created" value="RGVsbDtERVNLVE9QLTBMU0xBN0s7MjAyMC0wMi0yODswNDowNzoxMiBQTTsyNzIw"/>
        <attribute name="edited" value="RGVsbDtERVNLVE9QLTBMU0xBN0s7MjAyMC0wMi0yODswNDo1OTowNiBQTTsxOzI4Mzg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n" type="Integer" array="False" size=""/>
            <output expression="&quot; Nhap n:&quot;" newline="True"/>
            <input variable="n"/>
            <declare name="i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <declare name="F" type="Integer" array="True" size="n"/>
            <for variable="i" start="0" end="n-1" direction="inc" step="1">
                <if expression="i=0 or i=1">
                    <then>
                        <assign variable="F[i]" expression="1"/>
                    </then>
                    <else>
                        <assign variable="F[i]" expression="F[i-1]+F[i-2]"/>
                    </else>
                </if>
                <output expression="F[i]" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>
