#!/usr/bin/python3

import os

def generate_invitations(template: str, attendees: list[dict]):
    
    if template is None or template == "":
        print("Template is empty, no output files generated.")
        os.abort()
    
    if not isinstance(attendees, list[dict]):
        print("No data provided, no output files generated.")
        os.abort()
    
    if all(isinstance(valor, dict) for valor in attendees):
        print("No data provided, no output files generated.")
        os.abort()
            
    
    """ Iterate over the list of attendees and replace the placeholders in the template with the corresponding values from each attendee’s dictionary.
        If a value is missing, replace it with “N/A”.
    """
    
    i = 1
    
    for attendee in attendees:
        
        templateModified = template
        
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            
            forReplace = "{" + key + "}"
            
            templateModified = templateModified.replace(forReplace, attendee.get(key, "N/A"))
            
        fileModified = open("output_" + str(i) + ".txt", "w")
        fileModified.write(templateModified)
        fileModified.close()
            
        i += 1