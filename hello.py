djtext=djtext.lower()
        analyzed="" 
        for char in range(0,len(djtext)):
    
            if djtext[char] not in analyzed:
                analyzed = analyzed + djtext[char]
                print(f"{djtext[char]} : {djtext.count(djtext[char])}")