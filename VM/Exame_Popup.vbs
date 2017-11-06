result = MsgBox ("File Save Error", _
    vbAbortRetryIgnore+vbExclamation+vbDefaultButton2, "File Save Error")

Dim message

Select Case result
Case vbAbort
    message = "You chose Abort"
Case vbRetry
    message = "You chose Retry"
Case vbIgnore
    message = "Don't ignore me"
End Select

MsgBox message, vbInformation