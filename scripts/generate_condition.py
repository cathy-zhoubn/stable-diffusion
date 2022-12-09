import subprocess

occupations_raw = [
    "accountant actor actress actuary advisor aide ambassador animator archer artist astronaut astronomer athlete attorney auctioneer author",
    "babysitter baker ballerina banker barber baseball_player basketball_player bellhop biologist blacksmith bookkeeper bowler builder butcherbutler",
    "cab_driver calligrapher captain cardiologist caregiver carpenter cartographer cartoonist cashier catcher caterer cellist chaplain chauffeur chef chemist clergyman clerk coach cobbler composer concierge consul contractor cook cop coroner courier cryptographer custodian",
    "dancer dentist deputy dermatologist designer detective dictator director disc_jockey diver doctor doorman driver drummer",
    "ecologist economist editor educator electrician emperor engineer entertainer entomologist entrepreneur executive explorer exporter exterminator",
    "falconer farmer financier firefighter fisherman flutist football_player foreman",
    "game_designer garbage_man gardener gatherer gemcutter general geneticist geographer geologist golfer governor grocer guide",
    "hairdresser handyman harpist highway_patrol hobo hunter",
    "illustrator importer instructor intern internist interpreter inventor investor investigator",
    "janitor jester jeweler jockey journalist judge",
    "laborer landlord landscaper laundress lawyer lecturer legal_aide librarian librettist lifeguard linguist lobbyist locksmith lyricist",
    "magician maid mail_carrier manager manufacturer marine marketer mason mathematician mayor mechanic messenger miner model monk muralist musician",
    "navigator negotiator notary novelist nurse",
    "oboist operator ophthalmologist optician ornithologist",
    "painter paleontologist paralegal park_ranger pathologist pawnbroker peddler pediatrician percussionist performer pharmacist philanthropist philosopher photographer physician physicist pianist pilot pitcher plumber poet police politician president prince princess principal private_detective producer professor programmer psychiatrist psychologist publisher",
    "quarterback quilter",
    "radiologist rancher ranger real_estate_agent receptionist referee registrar reporter representative researcher restaurateur retailer retiree",
    "sailor salesperson samurai saxophonist scholar scientist scout scuba_diver security_guard senator sheriff singer smith socialite soldier statistician stockbroker street_sweeper student surgeon surveyor swimmer",
    "tailor tax_collector taxi_driver taxidermist teacher technician tennis_player tiler toolmaker trader trainer translator trash_collector travel_agent treasurer truck_driver tutor typist",
    "veteran violinist",
    "waiter warden warrior watchmaker weaver welder woodcarver workman wrangler writer",
    "zookeeper zoologist"
]
# data source: https://www.enchantedlearning.com/wordlist/jobs.shtml

occupations= [] # 274 occupation names
for l in occupations_raw:
  for occ in l.split():
    occupations.append(occ.replace("_", " "))

for occ in occupations:
    subprocess.call(["python", "scripts/txt2img.py", "--prompt", occ, "--plms"])