result = MsgBox ("File Save Error", _
    vbAbortRetryIgnore+vbExclamation+vbDefaultButton2, "File Save Error")

Dim message

'Determine which path the user picked'
Select Case result
Case vbAbort
    message = "You chose Abort"
Case vbRetry
    message = "You chose Retry"
Case vbIgnore
    message = "Don't ignore me"
End Select

'Start part two of the dialogue prompt'
result2 = MsgBox(message, vbAbortRetryIgnore+vbExclamation+vbDefaultButton2, "File Save Error")

Select Case result2
Case vbAbort
	message2 = "Abortv2"
Case vbRetry
	message2 = "Retryv2"
Case vbIgnore
	message2 = "Ignore v2"
End Select

'End the dialogue box with the final message'
MsgBox message2, vbInformation