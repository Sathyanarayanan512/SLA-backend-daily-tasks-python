class IntermediateQuittingError(Exception):
    pass

def enquiry():
    try:
        purpose_done=input("Your Purpose done? 'yes' or 'no': ")
        if purpose_done.lower()=='yes':
            print('Yes, you can get in. Cheers!')
        elif purpose_done.lower()=='no':
            raise IntermediateQuittingError("Attempt to do unauthorized quitting: responsibilities must have been fulfilled!!")
        else:
            print("Enter either 'yes' or 'no'")
            enquiry()
    except Exception as exception:
        print("You're ineligible -> ",exception)
enquiry()

