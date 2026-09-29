2xconst { Resolution } = require('@unstoppabledomains/resolution');
const resolution = new Resolution();

resolution.addr('robdoe.com', 'ETH')
    .then((address) => console.log('Owner ETH Address:', address))
    .catch((error) => console.error('Resolution Error:', error.message));
