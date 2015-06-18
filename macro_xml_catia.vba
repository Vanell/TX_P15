Sub CATMain()

'Définition du document de travail
Set productDocument1 = CATIA.ActiveDocument
Set product1 = productDocument1.Product
Set products1 = product1.Products

'Definition des variables utilisées
Dim w As Double
Dim p As Double
Dim r As Double
Dim PI As Double
PI = 4 * Atn(1)
Dim i As Integer

'Création du XML, entête
Set xmlDoc = CreateObject("Microsoft.XMLDOM")
Set oCreation = xmlDoc.createProcessingInstruction("xml", "version='1.0' encoding='ISO-8859-1'")
xmlDoc.InsertBefore oCreation, xmlDoc.childNodes.Item(0)
Set root = xmlDoc.createElement("PRODUCT")
xmlDoc.appendChild (root)

For i = 1 To products1.Count
    Set product2 = products1.Item(i)
    Dim myArray(11)
    product2.Position.GetComponents myArray
   
    'Calcul des angles en radian
        'Rotation suivant Y
    If (1 - (myArray(6)) * (myArray(6)) <= 0.000000000001) And (1 - (myArray(6)) * (myArray(6)) >= -0.000000000001) Then
        If myArray(6) > 0 Then
            p = PI / 2
        End If
        If myArray(6) < 0 Then
            p = -PI / 2
        End If
    Else
        p = Atn(myArray(6) / Sqr(1 - (myArray(6)) * (myArray(6))))
    End If
        
        'Rotation suivant X
    If ((myArray(8) / Cos(p)) <= 0.000000000001) And ((myArray(8) / Cos(p)) >= -0.000000000001) Then
        w = PI / 2
    Else
        If myArray(8) <= 0.000000000001 And myArray(8) >= -0.000000000001 Then
            w = PI / 2
        ElseIf Cos(p) <= 0.000000000001 And Cos(p) >= -0.000000000001 Then
            w = 0
        Else
            w = Atn(Sqr(1 - (myArray(8) / Cos(p)) * (myArray(8) / Cos(p))) / (myArray(8) / Cos(p)))
        End If
    End If
        
        'Rotation suivant Z
    If ((myArray(0) / Cos(p)) <= 0.000000000001) And ((myArray(0) / Cos(p)) >= -0.000000000001) Then
        r = PI / 2
    Else
        If myArray(0) <= 0.000000000001 And myArray(0) >= -0.000000000001 Then
            r = PI / 2
        ElseIf Cos(p) <= 0.000000000001 And Cos(p) >= -0.000000000001 Then
            r = 0
        Else
            r = Atn(Sqr(1 - (myArray(0) / Cos(p)) * (myArray(0) / Cos(p))) / (myArray(0) / Cos(p)))
        End If
    End If

    'Angle en Rad vers Deg
    p = (p * 180 / PI) Mod 180
    r = (r * 180 / PI) Mod 180
    w = (w * 180 / PI) Mod 180
    
'Création de la ligne de coordonnées XML
    If myArray(11) <> 0 Then
        Set posiElmt = xmlDoc.createElement("POSI")
        posiElmt.SetAttribute "x", Round(myArray(9), 2)
        posiElmt.SetAttribute "y", Round(myArray(10), 2)
        posiElmt.SetAttribute "z", Round(myArray(11), 2)
        posiElmt.SetAttribute "w", Round(w, 2)
        posiElmt.SetAttribute "p", Round(p, 2)
        posiElmt.SetAttribute "r", Round(r, 2)
        posiElmt.SetAttribute "config_data", "N, ,0,0"
        root.appendChild (posiElmt)
    End If

Next i

Set rdr = CreateObject("MSXML2.SAXXMLReader")
Set wrt = CreateObject("MSXML2.MXXMLWriter")
Set oStream = CreateObject("ADODB.STREAM")
oStream.Open
oStream.Charset = "ISO-8859-1"
 
wrt.indent = True
wrt.Encoding = "ISO-8859-1"
wrt.Output = oStream
Set rdr.contentHandler = wrt
Set rdr.errorHandler = wrt
rdr.Parse xmlDoc
wrt.Flush
 
oStream.SaveToFile product1.Name & ".xml", 2
 
Set rdr = Nothing
Set wrt = Nothing
Set xmlDoc = Nothing

'Dim objUserEnvVars As Object
'Set objUserEnvVars = CreateObject("WScript.Shell").Environment("filenamexml")
'objUserEnvVars.Item("filename") = product1.Name & ".xml"
'MsgBox (objUserEnvVars.Item)

'SetEnvironmentVariable "filenamexml", "filename"
'MsgBox (Environ("filenamexml"))


'Lancement du fichier tri python
Dim RetVal As Variant
Dim stExecute As String: stExecute = """C:\Python33\python.exe"""
Dim stFile As String: stFile = "c:\Users\Haytham\Desktop\tri_macro.py " & product1.Name & ".xml"
Dim stFull As String: stFull = stExecute & " " & stFile

RetVal = Shell(stFull & " DISPLAY", vbNormalFocus)

End Sub