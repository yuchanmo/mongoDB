db = db.getSiblingDB('repl');

var start = (new Date()).getTime();

for (var i = 0; i < 10000; i++) {
    db.journal_test.insertOne({'id': i, 'content': 'hello~'})
}

var end = (new Date()).getTime();

print(end - start);