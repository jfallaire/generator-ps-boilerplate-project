FROM python:3.7-alpine AS iow
WORKDIR /usr/local/app
COPY iow/requirements.txt ./
COPY src/platform/extensionRunner/requirements.txt ./requirements_extension.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements_extension.txt

FROM node:12-alpine AS base
ENV CHROME_BIN="/usr/bin/chromium-browser"\
    PUPPETEER_SKIP_CHROMIUM_DOWNLOAD="true"
WORKDIR /usr/src/app

RUN set -x \
    && apk update \
    && apk upgrade \
    && apk add --no-cache \
    git \
    openssh \
    dumb-init \
    udev \
    ttf-freefont \
    chromium \
    # Cleanup
    && apk del --no-cache make gcc g++ python binutils-gold gnupg libstdc++ \
    && rm -rf /usr/include \
    && rm -rf /var/cache/apk/* /root/.node-gyp /usr/share/man /tmp/* \
    && echo

COPY --from=iow / /
COPY docker-entrypoint.sh /usr/local/bin/
RUN npm install -g sfdx-cli gulp coveo-platform-client --silent
EXPOSE 3000
ENTRYPOINT ["/usr/bin/dumb-init", "docker-entrypoint.sh"]
CMD ["tail", "-f", "/dev/null"]