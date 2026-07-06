#!/usr/bin/env bash
#
# check-pack.sh — consistency checks for packs/70-business-specialists.
# Catches the bug class that structural lint can't: count drift.
#
#   1. Every "# ── Section (N)" header in agents.txt matches its line count
#   2. Every name in agents.txt (and agents-core-70.txt) resolves to a real
#      agent's frontmatter `name:` — no orphans, no typos
#   3. No duplicate names (the installer dedups silently, inflating counts)
#   4. Skill directories: frontmatter name == directory, "Use when" present
#   5. Doc claims match reality: skill counts quoted in BLUEPRINT.md,
#      README.md, skills/README.md vs. actual skill dirs
#
# Usage: ./scripts/check-pack.sh        (from repo root; exits non-zero on failure)

set -uo pipefail
cd "$(dirname "$0")/.."

PACK=packs/70-business-specialists
DIVS=(academic design engineering finance game-development gis marketing paid-media
      product project-management sales security spatial-computing specialized support testing)
errors=0
fail() { echo "FAIL: $1"; errors=$((errors + 1)); }

# --- collect all real agent names (lowercased) --------------------------------
ALL_NAMES=$(mktemp)
for d in "${DIVS[@]}"; do
  find "$d" -name '*.md' 2>/dev/null | while read -r f; do
    [[ "$(head -1 "$f")" == "---" ]] || continue
    awk '/^---$/{fm++;next} fm==1 && /^name: /{sub("^name: ",""); print tolower($0); exit}' "$f"
  done
done | sort > "$ALL_NAMES"

# --- 1+2+3: agents.txt sections, name resolution, duplicates ------------------
for LIST in "$PACK/agents.txt" "$PACK/agents-core-70.txt"; do
  [[ -f "$LIST" ]] || { fail "$LIST missing"; continue; }

  # duplicates
  dups=$(awk '!/^#/ && NF {gsub(/\r/,""); print tolower($0)}' "$LIST" | sort | uniq -d)
  [[ -n "$dups" ]] && fail "$LIST duplicate names: $dups"

  # every name resolves
  while IFS= read -r line; do
    [[ "$line" =~ ^#|^$ ]] && continue
    lname=$(echo "$line" | tr -d '\r' | tr '[:upper:]' '[:lower:]')
    grep -qxF "$lname" "$ALL_NAMES" || fail "$LIST name does not resolve: $line"
  done < "$LIST"
done

# section header counts (agents.txt only; headers look like "# ── Title (N)")
awk '
  /^# ── .*\([0-9]+\)/ {
    if (section != "") printf "%s\t%d\t%d\n", section, expected, count
    if (match($0, /\([0-9]+\)/)) expected = substr($0, RSTART + 1, RLENGTH - 2)
    section = $0; count = 0; next
  }
  /^# / || /^$/ { next }
  NF { count++ }
  END { if (section != "") printf "%s\t%d\t%d\n", section, expected, count }
' packs/70-business-specialists/agents.txt | while IFS=$'\t' read -r sec exp got; do
  [[ "$exp" == "$got" ]] || fail "agents.txt section count: '$sec' says ($exp) but has $got"
done

# --- 4: skills ----------------------------------------------------------------
nskills=0
for d in "$PACK"/skills/*/; do
  s="$d/SKILL.md"
  [[ -f "$s" ]] || continue
  nskills=$((nskills + 1))
  dir=$(basename "$d")
  n=$(awk '/^---$/{fm++;next} fm==1 && /^name: /{sub("^name: ",""); print; exit}' "$s")
  [[ "$n" == "$dir" ]] || fail "skill $dir: frontmatter name '$n' != directory"
  grep -q "Use when" "$s" || fail "skill $dir: description missing 'Use when' triggers"
done

# --- 5: doc claims vs reality ---------------------------------------------------
for doc in "$PACK/BLUEPRINT.md" "$PACK/README.md" "$PACK/skills/README.md"; do
  [[ -f "$doc" ]] || continue
  claims=$(grep -oE '[0-9]+ (one-command workflows|skills)' "$doc" | grep -oE '^[0-9]+' | sort -u)
  for c in $claims; do
    [[ "$c" == "$nskills" ]] || fail "$doc claims $c skills; actual: $nskills"
  done
done

rm -f "$ALL_NAMES"
if [[ $errors -eq 0 ]]; then
  echo "check-pack: all consistency checks PASSED ($nskills skills)"
else
  echo "check-pack: $errors failure(s)"
  exit 1
fi
