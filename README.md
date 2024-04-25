# plot-earthquake-data
plot Earthquake data on map

## Objective: 
We aimed to retrieve earthquake data, parse it, and display specific columns ('mag', 'place', and 'time') in a tabular format using Python.

# Topic:
Retrieving, Parsing, and Displaying Earthquake Data in Python

## Steps:

    Data Retrieval: 
        We assumed the earthquake data was obtained from a source such as the USGS Earthquake API or another provider.
    Data Parsing: 
        Utilized pandas to convert the earthquake data into a DataFrame for easier manipulation and display.
    Nested Data Handling: 
        Extracted required columns ('mag', 'place', 'time') nested within the 'properties' dictionary of each earthquake event using lambda functions.
    Time Conversion: 
        Converted time from milliseconds to a human-readable format ('YYYY-MM-DD HH:MM:SS') using the pd.to_datetime() function and string formatting.
    Display: 
        Presented the extracted columns in tabular format.
    Adjustments: 
        Made necessary adjustments based on error feedback to ensure correct indexing and handling of nested data.
    Verification: Verified the code produced the desired output.


<img width="1202" alt="image" src="https://github.com/bigheadG/plot-earthquake-data/assets/2010446/821b21db-5f45-4c64-94fe-47524b81106e">

<img width="501" alt="image" src="https://github.com/bigheadG/plot-earthquake-data/assets/2010446/a7225003-9ea2-4302-97e0-e44319a1978b">

