# cloudflare-ddns
Python script to update Cloudflare record with public dynamic IP

# usage
1. Create zone and record to be updated on Cloudflare.
1. Add environment variables to `.env` file:
    - CLOUDFLARE_API_KEY
    - CLOUDFLARE_ZONE_ID
    - CLOUDFLARE_RECORD_ID
1. Run `python3 cloudflare-ddns.py` recurrently in crontab to keep the record updated.