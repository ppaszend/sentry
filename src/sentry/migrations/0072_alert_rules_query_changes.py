# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-01 23:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sentry.db.models.fields.bounded
import sentry.db.models.fields.foreignkey


class Migration(migrations.Migration):
    # This flag is used to mark that a migration shouldn't be automatically run in
    # production. We set this to True for operations that we think are risky and want
    # someone from ops to run manually and monitor.
    # General advice is that if in doubt, mark your migration as `is_dangerous`.
    # Some things you should always mark as dangerous:
    # - Large data migrations. Typically we want these to be run manually by ops so that
    #   they can be monitored. Since data migrations will now hold a transaction open
    #   this is even more important.
    # - Adding columns to highly active tables, even ones that are NULL.
    is_dangerous = False

    # This flag is used to decide whether to run this migration in a transaction or not.
    # By default we prefer to run in a transaction, but for migrations where you want
    # to `CREATE INDEX CONCURRENTLY` this needs to be set to False. Typically you'll
    # want to create an index concurrently when adding one to an existing table.
    atomic = True

    dependencies = [
        ("sentry", "0071_add_default_fields_model_subclass"),
    ]

    operations = [
        migrations.CreateModel(
            name="SnubaQuery",
            fields=[
                (
                    "id",
                    sentry.db.models.fields.bounded.BoundedBigAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("dataset", models.TextField()),
                ("query", models.TextField()),
                ("aggregate", models.TextField()),
                ("time_window", models.IntegerField()),
                ("resolution", models.IntegerField()),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "environment",
                    sentry.db.models.fields.foreignkey.FlexibleForeignKey(
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sentry.Environment",
                    ),
                ),
            ],
            options={
                "db_table": "sentry_snubaquery",
            },
        ),
        migrations.AlterField(
            model_name="alertrule",
            name="aggregation",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="alertrule",
            name="dataset",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="alertrule",
            name="query",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="alertrule",
            name="resolution",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="alertrule",
            name="time_window",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="querysubscription",
            name="aggregation",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="querysubscription",
            name="dataset",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="querysubscription",
            name="query",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="querysubscription",
            name="resolution",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="querysubscription",
            name="time_window",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="alertrule",
            name="snuba_query",
            field=sentry.db.models.fields.foreignkey.FlexibleForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="sentry.SnubaQuery",
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="querysubscription",
            name="snuba_query",
            field=sentry.db.models.fields.foreignkey.FlexibleForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscriptions",
                to="sentry.SnubaQuery",
            ),
        ),
    ]
