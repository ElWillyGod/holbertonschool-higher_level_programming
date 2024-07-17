#!/usr/bin/python3

import os

def generate_invitations(template: str, attendees: list[dict]):
    
    if not isinstance(template, str) or not template:
        return "Template is empty, no output files generated."
    
    if not isinstance(attendees, list):
        return "No data provided, no output files generated."
    
    if not all(isinstance(valor, dict) for valor in attendees):
        return "No data provided, no output files generated."
    
    i = 1
    
    for attendee in attendees:
        
        templateModified = template
        
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            
            forReplace = "{" + key + "}"
            
            templateModified = templateModified.replace(forReplace, attendee.get(key) or "N/A")

        with open('output_'+ str(i) +'.txt', 'w') as file:
            file.write(templateModified)
            
        i += 1