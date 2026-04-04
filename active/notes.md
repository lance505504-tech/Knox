# Project Notes

## Cape 31 CMS — Current State
- **Dev URL:** https://polite-bay-0d57fd203.6.azurestaticapps.net
- **Prod URL:** https://proud-pebble-0896e5503.2.azurestaticapps.net
- **Working file:** cape31-class-management.html (384KB, Node OK, audit clean)
- **Phase 2b:** Complete — scope/permissions, entry gates, regatta flags
- **Phase 2c:** Next to build — club accounts
- **Auth.js files uploaded:** CareCore middleware — NOT Cape 31. Filed for reference only.

## Open Build Items
- [ ] Phase 2c: Club accounts (club record, club user role, club login view, provisional results)
- [ ] Permission fix: canManageButtons() = Int Admin ONLY (not ExCom)
- [ ] IHC cert lock: one-time entry by owner, locked on save, amend requires written reason
- [ ] Boat manager role: positions=['boat_manager'] + managedBoatId

## Decisions
- Entry gates default ALL OFF. UK=all ON. Ratchet: region turns ON, Int Admin turns OFF.
- Button issuance: Admin ONLY. ExCom can amend with reason but cannot issue.
- Payments: Stripe (UK), PayPal elsewhere
- Vakaros: API discussion with their tech team scheduled
- Public results: yes, fed to regional websites → www.Cape31Class.org

## Review by 15 April 2026
- [ ] lance505504-tech/Cape31-Class repo — likely old, delete if not needed

## Links
- Class website: https://www.cape31class.com
- Existing CMS: https://cms.cape31class.com/measurement/
