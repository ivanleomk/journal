const POT_BOTTOM_Y = 585;
const POTS_TIMES = [
    {
        duration: 0.5 + Math.random() * 0.3,
        delay: 0,
    },
    {
        duration: 0.5 + Math.random() * 0.3,
        delay: 0.5,
    },
    {
        duration: 0.5 + Math.random() * 0.3,
        delay: 0.2,
    },
];
const masterTimeline = new TimelineMax();
