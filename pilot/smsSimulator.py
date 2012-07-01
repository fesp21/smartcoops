import re, csv

provinces = ['Abra','Agusan del Norte','Agusan del Sur','Aklan','Albay','Antique','Apayao','Aurora','Basilan','Bataan','Batanes','Batangas','Benguet','Biliran','Bohol','Bukidnon','Bulacan','Cagayan','Camarines Norte','Camarines Sur','Camiguin','Capiz','Catanduanes','Cavite','Cebu','Compostela Valley','Cotabato','Davao del Norte','Davao del Sur','Davao Oriental','Dinagat Islands','Eastern Samar','Guimaras','Ifugao','Ilocos Norte','Ilocos Sur','Iloilo','Isabela','Kalinga','La Union','Laguna','Lanao del Norte','Lanao del Sur','Leyte','Maguindanao','Marinduque','Masbate','Misamis Occidental','Misamis Oriental','Mountain Province','Negros Occidental','Negros Oriental','Northern Samar','Nueva Ecija','Nueva Vizcaya','Occidental Mindoro','Oriental Mindoro','Palawan','Pampanga','Pangasinan','Quezon','Quirino','Rizal','Romblon','Samar','Sarangani','Siquijor','Sorsogon','South Cotabato','Southern Leyte','Sultan Kudarat','Sulu','Surigao del Norte','Surigao del Sur','Tarlac','Tawi-Tawi','Zambales','Zamboanga del Norte','Zamboanga del Sur','Zamboanga Sibugay','Metro Manila']

prompt = 'Send SMS to +63 151 888 4444: '
raw_input(prompt)
s = 'no name'
while s.lower() != 'yes':
    print "\nHello, I notice that it is the first time you are using SMART Coops. Please reply to SMS with your name (ex: Capitan, Sergio).\n"
    name = raw_input(prompt)
    print "\nPleased to meet you "+name+". Did I get your name correctly? (you can reply yes or no). Note that SMS sent to SMART Coops are free of charge, so do not worry about your account balance.\n"
    s = raw_input(prompt)
s = 'no coop'
while s.lower != 'yes':
    print "\nGreat, thank you for confirming your name, "+name+". SMART Coop helps you find out about prices for crop inputs, crop produce, loans, and more. I see that you are sending me messages from near San Pablo, Languna. Which cooperative are you a member of? Type the corresponding number. 1) San Benito Multi Purpose Cooperative, 2) San Pablo Cooperative, 3) Los Banos Cooperative, 4) Other, 5) I am not a member of a cooperative\n"
    s = raw_input(prompt)
    if s in ['1', '2', '3']:
        print 'huarry'
        s = 'yes'
    else:
        print 'boohoo'
        
