cd /path/to/your/mobile-repo
(.venv) egor@egor-msi:~/KASUD/Nornikel_Audit$ git rev-parse --show-toplevel
/home/egor/KASUD/Nornikel_Audit

git checkout v0.14.20-ios
git branch --show-current
git rev-parse --verify v0.14.19-ios
git rev-parse --verify v0.14.20-ios
git diff --name-status v0.14.19-ios...v0.14.20-ios
git diff v0.14.19-ios...v0.14.20-ios > contractor_changes_ios.patch
