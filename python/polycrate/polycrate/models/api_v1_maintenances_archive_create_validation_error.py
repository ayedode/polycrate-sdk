from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_maintenances_archive_create_actual_availability_error_component import (
        ApiV1MaintenancesArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_additional_recipients_error_component import (
        ApiV1MaintenancesArchiveCreateAdditionalRecipientsErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_affected_host_ids_error_component import (
        ApiV1MaintenancesArchiveCreateAffectedHostIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_affected_pop_ids_error_component import (
        ApiV1MaintenancesArchiveCreateAffectedPopIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_affected_volume_ids_error_component import (
        ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_annotations_error_component import (
        ApiV1MaintenancesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_announcement_results_error_component import (
        ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_announcement_sent_error_component import (
        ApiV1MaintenancesArchiveCreateAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_archived_at_error_component import (
        ApiV1MaintenancesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_archived_by_error_component import (
        ApiV1MaintenancesArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_archived_error_component import (
        ApiV1MaintenancesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_archived_reason_error_component import (
        ApiV1MaintenancesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_created_by_component_error_component import (
        ApiV1MaintenancesArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_created_by_user_error_component import (
        ApiV1MaintenancesArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_criticality_error_component import (
        ApiV1MaintenancesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_debug_mode_error_component import (
        ApiV1MaintenancesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_discovery_enabled_error_component import (
        ApiV1MaintenancesArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_display_name_error_component import (
        ApiV1MaintenancesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_draft_error_component import (
        ApiV1MaintenancesArchiveCreateDraftErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_end_announcement_sent_error_component import (
        ApiV1MaintenancesArchiveCreateEndAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_end_error_component import (
        ApiV1MaintenancesArchiveCreateEndErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_kind_error_component import (
        ApiV1MaintenancesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_labels_error_component import (
        ApiV1MaintenancesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1MaintenancesArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_managed_by_content_type_error_component import (
        ApiV1MaintenancesArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_managed_by_object_id_error_component import (
        ApiV1MaintenancesArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_modified_by_user_error_component import (
        ApiV1MaintenancesArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_name_error_component import (
        ApiV1MaintenancesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_non_field_errors_error_component import (
        ApiV1MaintenancesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_notification_ended_sent_error_component import (
        ApiV1MaintenancesArchiveCreateNotificationEndedSentErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_notification_scheduled_sent_error_component import (
        ApiV1MaintenancesArchiveCreateNotificationScheduledSentErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_notification_started_sent_error_component import (
        ApiV1MaintenancesArchiveCreateNotificationStartedSentErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_organization_id_error_component import (
        ApiV1MaintenancesArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_platform_dns_record_created_error_component import (
        ApiV1MaintenancesArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_platform_service_error_component import (
        ApiV1MaintenancesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_project_id_error_component import (
        ApiV1MaintenancesArchiveCreateProjectIdErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_provider_entity_error_component import (
        ApiV1MaintenancesArchiveCreateProviderEntityErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_provider_error_component import (
        ApiV1MaintenancesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_provider_id_error_component import (
        ApiV1MaintenancesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_provider_reference_error_component import (
        ApiV1MaintenancesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_reconciliation_enabled_error_component import (
        ApiV1MaintenancesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_reference_url_error_component import (
        ApiV1MaintenancesArchiveCreateReferenceUrlErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_scope_error_component import (
        ApiV1MaintenancesArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_sla_availability_error_component import (
        ApiV1MaintenancesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_sla_target_error_component import (
        ApiV1MaintenancesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_sla_window_days_error_component import (
        ApiV1MaintenancesArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_slo_availability_error_component import (
        ApiV1MaintenancesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_slo_target_error_component import (
        ApiV1MaintenancesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_slo_window_days_error_component import (
        ApiV1MaintenancesArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_source_datasource_error_component import (
        ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_source_item_id_error_component import (
        ApiV1MaintenancesArchiveCreateSourceItemIdErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_start_announcement_sent_error_component import (
        ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_start_error_component import (
        ApiV1MaintenancesArchiveCreateStartErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_target_availability_error_component import (
        ApiV1MaintenancesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_timeline_error_component import (
        ApiV1MaintenancesArchiveCreateTimelineErrorComponent,
    )
    from ..models.api_v1_maintenances_archive_create_workspace_id_error_component import (
        ApiV1MaintenancesArchiveCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1MaintenancesArchiveCreateValidationError")


@_attrs_define
class ApiV1MaintenancesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1MaintenancesArchiveCreateActualAvailabilityErrorComponent |
            ApiV1MaintenancesArchiveCreateAdditionalRecipientsErrorComponent |
            ApiV1MaintenancesArchiveCreateAffectedHostIdsErrorComponent |
            ApiV1MaintenancesArchiveCreateAffectedPopIdsErrorComponent |
            ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponent |
            ApiV1MaintenancesArchiveCreateAnnotationsErrorComponent |
            ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponent |
            ApiV1MaintenancesArchiveCreateAnnouncementSentErrorComponent |
            ApiV1MaintenancesArchiveCreateArchivedAtErrorComponent | ApiV1MaintenancesArchiveCreateArchivedByErrorComponent
            | ApiV1MaintenancesArchiveCreateArchivedErrorComponent |
            ApiV1MaintenancesArchiveCreateArchivedReasonErrorComponent |
            ApiV1MaintenancesArchiveCreateCreatedByComponentErrorComponent |
            ApiV1MaintenancesArchiveCreateCreatedByUserErrorComponent |
            ApiV1MaintenancesArchiveCreateCriticalityErrorComponent | ApiV1MaintenancesArchiveCreateDebugModeErrorComponent
            | ApiV1MaintenancesArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1MaintenancesArchiveCreateDisplayNameErrorComponent | ApiV1MaintenancesArchiveCreateDraftErrorComponent |
            ApiV1MaintenancesArchiveCreateEndAnnouncementSentErrorComponent |
            ApiV1MaintenancesArchiveCreateEndErrorComponent | ApiV1MaintenancesArchiveCreateKindErrorComponent |
            ApiV1MaintenancesArchiveCreateLabelsErrorComponent |
            ApiV1MaintenancesArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1MaintenancesArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1MaintenancesArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1MaintenancesArchiveCreateModifiedByUserErrorComponent | ApiV1MaintenancesArchiveCreateNameErrorComponent |
            ApiV1MaintenancesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1MaintenancesArchiveCreateNotificationEndedSentErrorComponent |
            ApiV1MaintenancesArchiveCreateNotificationScheduledSentErrorComponent |
            ApiV1MaintenancesArchiveCreateNotificationStartedSentErrorComponent |
            ApiV1MaintenancesArchiveCreateOrganizationIdErrorComponent |
            ApiV1MaintenancesArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1MaintenancesArchiveCreatePlatformServiceErrorComponent |
            ApiV1MaintenancesArchiveCreateProjectIdErrorComponent |
            ApiV1MaintenancesArchiveCreateProviderEntityErrorComponent |
            ApiV1MaintenancesArchiveCreateProviderErrorComponent | ApiV1MaintenancesArchiveCreateProviderIdErrorComponent |
            ApiV1MaintenancesArchiveCreateProviderReferenceErrorComponent |
            ApiV1MaintenancesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1MaintenancesArchiveCreateReferenceUrlErrorComponent | ApiV1MaintenancesArchiveCreateScopeErrorComponent |
            ApiV1MaintenancesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1MaintenancesArchiveCreateSlaTargetErrorComponent |
            ApiV1MaintenancesArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1MaintenancesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1MaintenancesArchiveCreateSloTargetErrorComponent |
            ApiV1MaintenancesArchiveCreateSloWindowDaysErrorComponent |
            ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponent |
            ApiV1MaintenancesArchiveCreateSourceItemIdErrorComponent |
            ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponent |
            ApiV1MaintenancesArchiveCreateStartErrorComponent |
            ApiV1MaintenancesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1MaintenancesArchiveCreateTimelineErrorComponent |
            ApiV1MaintenancesArchiveCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1MaintenancesArchiveCreateActualAvailabilityErrorComponent
        | ApiV1MaintenancesArchiveCreateAdditionalRecipientsErrorComponent
        | ApiV1MaintenancesArchiveCreateAffectedHostIdsErrorComponent
        | ApiV1MaintenancesArchiveCreateAffectedPopIdsErrorComponent
        | ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponent
        | ApiV1MaintenancesArchiveCreateAnnotationsErrorComponent
        | ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponent
        | ApiV1MaintenancesArchiveCreateAnnouncementSentErrorComponent
        | ApiV1MaintenancesArchiveCreateArchivedAtErrorComponent
        | ApiV1MaintenancesArchiveCreateArchivedByErrorComponent
        | ApiV1MaintenancesArchiveCreateArchivedErrorComponent
        | ApiV1MaintenancesArchiveCreateArchivedReasonErrorComponent
        | ApiV1MaintenancesArchiveCreateCreatedByComponentErrorComponent
        | ApiV1MaintenancesArchiveCreateCreatedByUserErrorComponent
        | ApiV1MaintenancesArchiveCreateCriticalityErrorComponent
        | ApiV1MaintenancesArchiveCreateDebugModeErrorComponent
        | ApiV1MaintenancesArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1MaintenancesArchiveCreateDisplayNameErrorComponent
        | ApiV1MaintenancesArchiveCreateDraftErrorComponent
        | ApiV1MaintenancesArchiveCreateEndAnnouncementSentErrorComponent
        | ApiV1MaintenancesArchiveCreateEndErrorComponent
        | ApiV1MaintenancesArchiveCreateKindErrorComponent
        | ApiV1MaintenancesArchiveCreateLabelsErrorComponent
        | ApiV1MaintenancesArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1MaintenancesArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1MaintenancesArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1MaintenancesArchiveCreateModifiedByUserErrorComponent
        | ApiV1MaintenancesArchiveCreateNameErrorComponent
        | ApiV1MaintenancesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1MaintenancesArchiveCreateNotificationEndedSentErrorComponent
        | ApiV1MaintenancesArchiveCreateNotificationScheduledSentErrorComponent
        | ApiV1MaintenancesArchiveCreateNotificationStartedSentErrorComponent
        | ApiV1MaintenancesArchiveCreateOrganizationIdErrorComponent
        | ApiV1MaintenancesArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1MaintenancesArchiveCreatePlatformServiceErrorComponent
        | ApiV1MaintenancesArchiveCreateProjectIdErrorComponent
        | ApiV1MaintenancesArchiveCreateProviderEntityErrorComponent
        | ApiV1MaintenancesArchiveCreateProviderErrorComponent
        | ApiV1MaintenancesArchiveCreateProviderIdErrorComponent
        | ApiV1MaintenancesArchiveCreateProviderReferenceErrorComponent
        | ApiV1MaintenancesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1MaintenancesArchiveCreateReferenceUrlErrorComponent
        | ApiV1MaintenancesArchiveCreateScopeErrorComponent
        | ApiV1MaintenancesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1MaintenancesArchiveCreateSlaTargetErrorComponent
        | ApiV1MaintenancesArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1MaintenancesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1MaintenancesArchiveCreateSloTargetErrorComponent
        | ApiV1MaintenancesArchiveCreateSloWindowDaysErrorComponent
        | ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponent
        | ApiV1MaintenancesArchiveCreateSourceItemIdErrorComponent
        | ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponent
        | ApiV1MaintenancesArchiveCreateStartErrorComponent
        | ApiV1MaintenancesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1MaintenancesArchiveCreateTimelineErrorComponent
        | ApiV1MaintenancesArchiveCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_maintenances_archive_create_actual_availability_error_component import (
            ApiV1MaintenancesArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_additional_recipients_error_component import (
            ApiV1MaintenancesArchiveCreateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_affected_host_ids_error_component import (
            ApiV1MaintenancesArchiveCreateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_affected_pop_ids_error_component import (
            ApiV1MaintenancesArchiveCreateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_affected_volume_ids_error_component import (
            ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_annotations_error_component import (
            ApiV1MaintenancesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_announcement_results_error_component import (
            ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_announcement_sent_error_component import (
            ApiV1MaintenancesArchiveCreateAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_archived_at_error_component import (
            ApiV1MaintenancesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_archived_by_error_component import (
            ApiV1MaintenancesArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_archived_error_component import (
            ApiV1MaintenancesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_archived_reason_error_component import (
            ApiV1MaintenancesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_created_by_component_error_component import (
            ApiV1MaintenancesArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_created_by_user_error_component import (
            ApiV1MaintenancesArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_criticality_error_component import (
            ApiV1MaintenancesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_debug_mode_error_component import (
            ApiV1MaintenancesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_discovery_enabled_error_component import (
            ApiV1MaintenancesArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_display_name_error_component import (
            ApiV1MaintenancesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_draft_error_component import (
            ApiV1MaintenancesArchiveCreateDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_end_announcement_sent_error_component import (
            ApiV1MaintenancesArchiveCreateEndAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_end_error_component import (
            ApiV1MaintenancesArchiveCreateEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_kind_error_component import (
            ApiV1MaintenancesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_labels_error_component import (
            ApiV1MaintenancesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1MaintenancesArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_managed_by_content_type_error_component import (
            ApiV1MaintenancesArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_managed_by_object_id_error_component import (
            ApiV1MaintenancesArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_modified_by_user_error_component import (
            ApiV1MaintenancesArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_name_error_component import (
            ApiV1MaintenancesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_non_field_errors_error_component import (
            ApiV1MaintenancesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_notification_ended_sent_error_component import (
            ApiV1MaintenancesArchiveCreateNotificationEndedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_notification_scheduled_sent_error_component import (
            ApiV1MaintenancesArchiveCreateNotificationScheduledSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_notification_started_sent_error_component import (
            ApiV1MaintenancesArchiveCreateNotificationStartedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_organization_id_error_component import (
            ApiV1MaintenancesArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_platform_dns_record_created_error_component import (
            ApiV1MaintenancesArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_platform_service_error_component import (
            ApiV1MaintenancesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_project_id_error_component import (
            ApiV1MaintenancesArchiveCreateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_provider_entity_error_component import (
            ApiV1MaintenancesArchiveCreateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_provider_error_component import (
            ApiV1MaintenancesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_provider_id_error_component import (
            ApiV1MaintenancesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_provider_reference_error_component import (
            ApiV1MaintenancesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_reconciliation_enabled_error_component import (
            ApiV1MaintenancesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_reference_url_error_component import (
            ApiV1MaintenancesArchiveCreateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_scope_error_component import (
            ApiV1MaintenancesArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_sla_availability_error_component import (
            ApiV1MaintenancesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_sla_target_error_component import (
            ApiV1MaintenancesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_sla_window_days_error_component import (
            ApiV1MaintenancesArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_slo_availability_error_component import (
            ApiV1MaintenancesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_slo_target_error_component import (
            ApiV1MaintenancesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_slo_window_days_error_component import (
            ApiV1MaintenancesArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_source_item_id_error_component import (
            ApiV1MaintenancesArchiveCreateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_start_announcement_sent_error_component import (
            ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_start_error_component import (
            ApiV1MaintenancesArchiveCreateStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_target_availability_error_component import (
            ApiV1MaintenancesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_timeline_error_component import (
            ApiV1MaintenancesArchiveCreateTimelineErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_workspace_id_error_component import (
            ApiV1MaintenancesArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateAffectedHostIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateAffectedPopIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1MaintenancesArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateSourceItemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateReferenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateEndAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateAdditionalRecipientsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateTimelineErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateNotificationScheduledSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateNotificationStartedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateNotificationEndedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesArchiveCreateProviderEntityErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_maintenances_archive_create_actual_availability_error_component import (
            ApiV1MaintenancesArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_additional_recipients_error_component import (
            ApiV1MaintenancesArchiveCreateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_affected_host_ids_error_component import (
            ApiV1MaintenancesArchiveCreateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_affected_pop_ids_error_component import (
            ApiV1MaintenancesArchiveCreateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_affected_volume_ids_error_component import (
            ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_annotations_error_component import (
            ApiV1MaintenancesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_announcement_results_error_component import (
            ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_announcement_sent_error_component import (
            ApiV1MaintenancesArchiveCreateAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_archived_at_error_component import (
            ApiV1MaintenancesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_archived_by_error_component import (
            ApiV1MaintenancesArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_archived_error_component import (
            ApiV1MaintenancesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_archived_reason_error_component import (
            ApiV1MaintenancesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_created_by_component_error_component import (
            ApiV1MaintenancesArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_created_by_user_error_component import (
            ApiV1MaintenancesArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_criticality_error_component import (
            ApiV1MaintenancesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_debug_mode_error_component import (
            ApiV1MaintenancesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_discovery_enabled_error_component import (
            ApiV1MaintenancesArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_display_name_error_component import (
            ApiV1MaintenancesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_draft_error_component import (
            ApiV1MaintenancesArchiveCreateDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_end_announcement_sent_error_component import (
            ApiV1MaintenancesArchiveCreateEndAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_end_error_component import (
            ApiV1MaintenancesArchiveCreateEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_kind_error_component import (
            ApiV1MaintenancesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_labels_error_component import (
            ApiV1MaintenancesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1MaintenancesArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_managed_by_content_type_error_component import (
            ApiV1MaintenancesArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_managed_by_object_id_error_component import (
            ApiV1MaintenancesArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_modified_by_user_error_component import (
            ApiV1MaintenancesArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_name_error_component import (
            ApiV1MaintenancesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_non_field_errors_error_component import (
            ApiV1MaintenancesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_notification_ended_sent_error_component import (
            ApiV1MaintenancesArchiveCreateNotificationEndedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_notification_scheduled_sent_error_component import (
            ApiV1MaintenancesArchiveCreateNotificationScheduledSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_notification_started_sent_error_component import (
            ApiV1MaintenancesArchiveCreateNotificationStartedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_organization_id_error_component import (
            ApiV1MaintenancesArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_platform_dns_record_created_error_component import (
            ApiV1MaintenancesArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_platform_service_error_component import (
            ApiV1MaintenancesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_project_id_error_component import (
            ApiV1MaintenancesArchiveCreateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_provider_entity_error_component import (
            ApiV1MaintenancesArchiveCreateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_provider_error_component import (
            ApiV1MaintenancesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_provider_id_error_component import (
            ApiV1MaintenancesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_provider_reference_error_component import (
            ApiV1MaintenancesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_reconciliation_enabled_error_component import (
            ApiV1MaintenancesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_reference_url_error_component import (
            ApiV1MaintenancesArchiveCreateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_scope_error_component import (
            ApiV1MaintenancesArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_sla_availability_error_component import (
            ApiV1MaintenancesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_sla_target_error_component import (
            ApiV1MaintenancesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_sla_window_days_error_component import (
            ApiV1MaintenancesArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_slo_availability_error_component import (
            ApiV1MaintenancesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_slo_target_error_component import (
            ApiV1MaintenancesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_slo_window_days_error_component import (
            ApiV1MaintenancesArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_source_datasource_error_component import (
            ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_source_item_id_error_component import (
            ApiV1MaintenancesArchiveCreateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_start_announcement_sent_error_component import (
            ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_start_error_component import (
            ApiV1MaintenancesArchiveCreateStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_target_availability_error_component import (
            ApiV1MaintenancesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_timeline_error_component import (
            ApiV1MaintenancesArchiveCreateTimelineErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_archive_create_workspace_id_error_component import (
            ApiV1MaintenancesArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1MaintenancesArchiveCreateActualAvailabilityErrorComponent
                | ApiV1MaintenancesArchiveCreateAdditionalRecipientsErrorComponent
                | ApiV1MaintenancesArchiveCreateAffectedHostIdsErrorComponent
                | ApiV1MaintenancesArchiveCreateAffectedPopIdsErrorComponent
                | ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponent
                | ApiV1MaintenancesArchiveCreateAnnotationsErrorComponent
                | ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponent
                | ApiV1MaintenancesArchiveCreateAnnouncementSentErrorComponent
                | ApiV1MaintenancesArchiveCreateArchivedAtErrorComponent
                | ApiV1MaintenancesArchiveCreateArchivedByErrorComponent
                | ApiV1MaintenancesArchiveCreateArchivedErrorComponent
                | ApiV1MaintenancesArchiveCreateArchivedReasonErrorComponent
                | ApiV1MaintenancesArchiveCreateCreatedByComponentErrorComponent
                | ApiV1MaintenancesArchiveCreateCreatedByUserErrorComponent
                | ApiV1MaintenancesArchiveCreateCriticalityErrorComponent
                | ApiV1MaintenancesArchiveCreateDebugModeErrorComponent
                | ApiV1MaintenancesArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1MaintenancesArchiveCreateDisplayNameErrorComponent
                | ApiV1MaintenancesArchiveCreateDraftErrorComponent
                | ApiV1MaintenancesArchiveCreateEndAnnouncementSentErrorComponent
                | ApiV1MaintenancesArchiveCreateEndErrorComponent
                | ApiV1MaintenancesArchiveCreateKindErrorComponent
                | ApiV1MaintenancesArchiveCreateLabelsErrorComponent
                | ApiV1MaintenancesArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1MaintenancesArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1MaintenancesArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1MaintenancesArchiveCreateModifiedByUserErrorComponent
                | ApiV1MaintenancesArchiveCreateNameErrorComponent
                | ApiV1MaintenancesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1MaintenancesArchiveCreateNotificationEndedSentErrorComponent
                | ApiV1MaintenancesArchiveCreateNotificationScheduledSentErrorComponent
                | ApiV1MaintenancesArchiveCreateNotificationStartedSentErrorComponent
                | ApiV1MaintenancesArchiveCreateOrganizationIdErrorComponent
                | ApiV1MaintenancesArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1MaintenancesArchiveCreatePlatformServiceErrorComponent
                | ApiV1MaintenancesArchiveCreateProjectIdErrorComponent
                | ApiV1MaintenancesArchiveCreateProviderEntityErrorComponent
                | ApiV1MaintenancesArchiveCreateProviderErrorComponent
                | ApiV1MaintenancesArchiveCreateProviderIdErrorComponent
                | ApiV1MaintenancesArchiveCreateProviderReferenceErrorComponent
                | ApiV1MaintenancesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1MaintenancesArchiveCreateReferenceUrlErrorComponent
                | ApiV1MaintenancesArchiveCreateScopeErrorComponent
                | ApiV1MaintenancesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1MaintenancesArchiveCreateSlaTargetErrorComponent
                | ApiV1MaintenancesArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1MaintenancesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1MaintenancesArchiveCreateSloTargetErrorComponent
                | ApiV1MaintenancesArchiveCreateSloWindowDaysErrorComponent
                | ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponent
                | ApiV1MaintenancesArchiveCreateSourceItemIdErrorComponent
                | ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponent
                | ApiV1MaintenancesArchiveCreateStartErrorComponent
                | ApiV1MaintenancesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1MaintenancesArchiveCreateTimelineErrorComponent
                | ApiV1MaintenancesArchiveCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_0 = (
                        ApiV1MaintenancesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_1 = (
                        ApiV1MaintenancesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_2 = (
                        ApiV1MaintenancesArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_3 = (
                        ApiV1MaintenancesArchiveCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_4 = (
                        ApiV1MaintenancesArchiveCreateProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_5 = (
                        ApiV1MaintenancesArchiveCreateAffectedHostIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_6 = (
                        ApiV1MaintenancesArchiveCreateAffectedVolumeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_7 = (
                        ApiV1MaintenancesArchiveCreateAffectedPopIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_8 = (
                        ApiV1MaintenancesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_9 = (
                        ApiV1MaintenancesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_10 = (
                        ApiV1MaintenancesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_11 = (
                        ApiV1MaintenancesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_12 = (
                        ApiV1MaintenancesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_13 = (
                        ApiV1MaintenancesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_14 = (
                        ApiV1MaintenancesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_15 = (
                        ApiV1MaintenancesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_16 = (
                        ApiV1MaintenancesArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_17 = (
                        ApiV1MaintenancesArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_18 = (
                        ApiV1MaintenancesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_19 = (
                        ApiV1MaintenancesArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_20 = (
                        ApiV1MaintenancesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_21 = (
                        ApiV1MaintenancesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_22 = (
                        ApiV1MaintenancesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_23 = (
                        ApiV1MaintenancesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_24 = (
                        ApiV1MaintenancesArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_25 = (
                        ApiV1MaintenancesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_26 = (
                        ApiV1MaintenancesArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_27 = (
                        ApiV1MaintenancesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_28 = (
                        ApiV1MaintenancesArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_29 = (
                        ApiV1MaintenancesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_30 = (
                        ApiV1MaintenancesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_31 = (
                        ApiV1MaintenancesArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_32 = (
                        ApiV1MaintenancesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_33 = (
                        ApiV1MaintenancesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_34 = (
                        ApiV1MaintenancesArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_35 = (
                        ApiV1MaintenancesArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_36 = (
                        ApiV1MaintenancesArchiveCreateStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_37 = (
                        ApiV1MaintenancesArchiveCreateEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_38 = (
                        ApiV1MaintenancesArchiveCreateDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_39 = (
                        ApiV1MaintenancesArchiveCreateSourceItemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_40 = (
                        ApiV1MaintenancesArchiveCreateReferenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_41 = (
                        ApiV1MaintenancesArchiveCreateAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_42 = (
                        ApiV1MaintenancesArchiveCreateStartAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_43 = (
                        ApiV1MaintenancesArchiveCreateEndAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_44 = (
                        ApiV1MaintenancesArchiveCreateAdditionalRecipientsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_45 = (
                        ApiV1MaintenancesArchiveCreateAnnouncementResultsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_46 = (
                        ApiV1MaintenancesArchiveCreateTimelineErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_47 = (
                        ApiV1MaintenancesArchiveCreateNotificationScheduledSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_48 = (
                        ApiV1MaintenancesArchiveCreateNotificationStartedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_49 = (
                        ApiV1MaintenancesArchiveCreateNotificationEndedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_50 = (
                        ApiV1MaintenancesArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_51 = (
                        ApiV1MaintenancesArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_52 = (
                        ApiV1MaintenancesArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_53 = (
                        ApiV1MaintenancesArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_archive_create_error_type_54 = (
                        ApiV1MaintenancesArchiveCreateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_archive_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenances_archive_create_error_type_55 = (
                    ApiV1MaintenancesArchiveCreateSourceDatasourceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_maintenances_archive_create_error_type_55

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_maintenances_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_maintenances_archive_create_validation_error.additional_properties = d
        return api_v1_maintenances_archive_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
