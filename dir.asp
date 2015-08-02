<%
' adapted from a script by 4guysfromrolla.com
dir = Request.QueryString("DIR") 'specify DIR= parameter in URI
Set fileSystemObject = CreateObject("Scripting.FileSystemObject")
Set actualDir = fileSystemObject.GetFolder(dir)  
Set dirContents = actualDir.Files 
Set subDir = actualDir.SubFolders 
For Each fileOrDir in subDir   
  Response.Write fileOrDir.name & "<br>"
Next  
Response.Write "<br>"
For Each fileOrDir in dirContents
  Response.Write fileOrDir.name & "<br>"
Next  
Set subDir = nothing
Set fileSystemObject = nothing
Set actualDir = nothing
Set dirContents = nothing
%>
