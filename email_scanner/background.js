chrome.runtime.onInstalled.addListener(() => {
    chrome.action.setBadgeText({
      text: "OFF",
    });
  });

const gmail = 'https://mail.google.com/mail/u/0/';
const outlook = 'https://outlook.live.com/mail/0/';

chrome.action.onClicked.addListener(async (tab) => {
  console.log(tab.url);
  if (tab.url.startsWith(gmail) || tab.url.startsWith(outlook)) {
    const prevState = await chrome.action.getBadgeText({ tabId: tab.id });
    const nextState = prevState === 'SCANNING' ? 'OFF' : 'SCANNING';

    await chrome.action.setBadgeText({
      tabId: tab.id,
      text: nextState,
    });

    if (nextState === "SCANNING") {
      await chrome.scripting.executeScript({
        target : {tabId : tab.id},
        files : [ "script.js" ],
      }).then(() => console.log("scanned email"));
    }

    await chrome.action.setBadgeText({
      tabId: tab.id,
      text: "OFF",
    });
  }
});

