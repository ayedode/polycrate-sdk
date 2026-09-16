from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_incidents_archive_create_actual_availability_error_component import (
        ApiV1IncidentsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_affected_host_ids_error_component import (
        ApiV1IncidentsArchiveCreateAffectedHostIdsErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_affected_pop_ids_error_component import (
        ApiV1IncidentsArchiveCreateAffectedPopIdsErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_affected_volume_ids_error_component import (
        ApiV1IncidentsArchiveCreateAffectedVolumeIdsErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_annotations_error_component import (
        ApiV1IncidentsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_archived_at_error_component import (
        ApiV1IncidentsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_archived_by_error_component import (
        ApiV1IncidentsArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_archived_error_component import (
        ApiV1IncidentsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_archived_reason_error_component import (
        ApiV1IncidentsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_created_by_component_error_component import (
        ApiV1IncidentsArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_created_by_user_error_component import (
        ApiV1IncidentsArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_criticality_error_component import (
        ApiV1IncidentsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_debug_mode_error_component import (
        ApiV1IncidentsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_discovered_at_error_component import (
        ApiV1IncidentsArchiveCreateDiscoveredAtErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_discovery_enabled_error_component import (
        ApiV1IncidentsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_display_name_error_component import (
        ApiV1IncidentsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_downtime_ids_error_component import (
        ApiV1IncidentsArchiveCreateDowntimeIdsErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_kind_error_component import (
        ApiV1IncidentsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_labels_error_component import (
        ApiV1IncidentsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1IncidentsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_managed_by_content_type_error_component import (
        ApiV1IncidentsArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_managed_by_object_id_error_component import (
        ApiV1IncidentsArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_modified_by_user_error_component import (
        ApiV1IncidentsArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_name_error_component import (
        ApiV1IncidentsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_non_field_errors_error_component import (
        ApiV1IncidentsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_notification_closed_sent_error_component import (
        ApiV1IncidentsArchiveCreateNotificationClosedSentErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_notification_opened_sent_error_component import (
        ApiV1IncidentsArchiveCreateNotificationOpenedSentErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_occurred_at_error_component import (
        ApiV1IncidentsArchiveCreateOccurredAtErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_organization_id_error_component import (
        ApiV1IncidentsArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_platform_dns_record_created_error_component import (
        ApiV1IncidentsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_platform_service_error_component import (
        ApiV1IncidentsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_provider_entity_error_component import (
        ApiV1IncidentsArchiveCreateProviderEntityErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_provider_error_component import (
        ApiV1IncidentsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_provider_id_error_component import (
        ApiV1IncidentsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_provider_reference_error_component import (
        ApiV1IncidentsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_reconciliation_enabled_error_component import (
        ApiV1IncidentsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_reference_url_error_component import (
        ApiV1IncidentsArchiveCreateReferenceUrlErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_reporter_error_component import (
        ApiV1IncidentsArchiveCreateReporterErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_resolved_at_error_component import (
        ApiV1IncidentsArchiveCreateResolvedAtErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_scope_error_component import (
        ApiV1IncidentsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_sla_availability_error_component import (
        ApiV1IncidentsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_sla_target_error_component import (
        ApiV1IncidentsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_sla_window_days_error_component import (
        ApiV1IncidentsArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_slo_availability_error_component import (
        ApiV1IncidentsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_slo_target_error_component import (
        ApiV1IncidentsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_slo_window_days_error_component import (
        ApiV1IncidentsArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_source_datasource_error_component import (
        ApiV1IncidentsArchiveCreateSourceDatasourceErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_source_item_id_error_component import (
        ApiV1IncidentsArchiveCreateSourceItemIdErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_status_error_component import (
        ApiV1IncidentsArchiveCreateStatusErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_target_availability_error_component import (
        ApiV1IncidentsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_vulnerability_finding_ids_error_component import (
        ApiV1IncidentsArchiveCreateVulnerabilityFindingIdsErrorComponent,
    )
    from ..models.api_v1_incidents_archive_create_workspace_id_error_component import (
        ApiV1IncidentsArchiveCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IncidentsArchiveCreateValidationError")


@_attrs_define
class ApiV1IncidentsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IncidentsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1IncidentsArchiveCreateAffectedHostIdsErrorComponent |
            ApiV1IncidentsArchiveCreateAffectedPopIdsErrorComponent |
            ApiV1IncidentsArchiveCreateAffectedVolumeIdsErrorComponent |
            ApiV1IncidentsArchiveCreateAnnotationsErrorComponent | ApiV1IncidentsArchiveCreateArchivedAtErrorComponent |
            ApiV1IncidentsArchiveCreateArchivedByErrorComponent | ApiV1IncidentsArchiveCreateArchivedErrorComponent |
            ApiV1IncidentsArchiveCreateArchivedReasonErrorComponent |
            ApiV1IncidentsArchiveCreateCreatedByComponentErrorComponent |
            ApiV1IncidentsArchiveCreateCreatedByUserErrorComponent | ApiV1IncidentsArchiveCreateCriticalityErrorComponent |
            ApiV1IncidentsArchiveCreateDebugModeErrorComponent | ApiV1IncidentsArchiveCreateDiscoveredAtErrorComponent |
            ApiV1IncidentsArchiveCreateDiscoveryEnabledErrorComponent | ApiV1IncidentsArchiveCreateDisplayNameErrorComponent
            | ApiV1IncidentsArchiveCreateDowntimeIdsErrorComponent | ApiV1IncidentsArchiveCreateKindErrorComponent |
            ApiV1IncidentsArchiveCreateLabelsErrorComponent |
            ApiV1IncidentsArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1IncidentsArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1IncidentsArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1IncidentsArchiveCreateModifiedByUserErrorComponent | ApiV1IncidentsArchiveCreateNameErrorComponent |
            ApiV1IncidentsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1IncidentsArchiveCreateNotificationClosedSentErrorComponent |
            ApiV1IncidentsArchiveCreateNotificationOpenedSentErrorComponent |
            ApiV1IncidentsArchiveCreateOccurredAtErrorComponent | ApiV1IncidentsArchiveCreateOrganizationIdErrorComponent |
            ApiV1IncidentsArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1IncidentsArchiveCreatePlatformServiceErrorComponent |
            ApiV1IncidentsArchiveCreateProviderEntityErrorComponent | ApiV1IncidentsArchiveCreateProviderErrorComponent |
            ApiV1IncidentsArchiveCreateProviderIdErrorComponent | ApiV1IncidentsArchiveCreateProviderReferenceErrorComponent
            | ApiV1IncidentsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1IncidentsArchiveCreateReferenceUrlErrorComponent | ApiV1IncidentsArchiveCreateReporterErrorComponent |
            ApiV1IncidentsArchiveCreateResolvedAtErrorComponent | ApiV1IncidentsArchiveCreateScopeErrorComponent |
            ApiV1IncidentsArchiveCreateSlaAvailabilityErrorComponent | ApiV1IncidentsArchiveCreateSlaTargetErrorComponent |
            ApiV1IncidentsArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1IncidentsArchiveCreateSloAvailabilityErrorComponent | ApiV1IncidentsArchiveCreateSloTargetErrorComponent |
            ApiV1IncidentsArchiveCreateSloWindowDaysErrorComponent |
            ApiV1IncidentsArchiveCreateSourceDatasourceErrorComponent |
            ApiV1IncidentsArchiveCreateSourceItemIdErrorComponent | ApiV1IncidentsArchiveCreateStatusErrorComponent |
            ApiV1IncidentsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1IncidentsArchiveCreateVulnerabilityFindingIdsErrorComponent |
            ApiV1IncidentsArchiveCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IncidentsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1IncidentsArchiveCreateAffectedHostIdsErrorComponent
        | ApiV1IncidentsArchiveCreateAffectedPopIdsErrorComponent
        | ApiV1IncidentsArchiveCreateAffectedVolumeIdsErrorComponent
        | ApiV1IncidentsArchiveCreateAnnotationsErrorComponent
        | ApiV1IncidentsArchiveCreateArchivedAtErrorComponent
        | ApiV1IncidentsArchiveCreateArchivedByErrorComponent
        | ApiV1IncidentsArchiveCreateArchivedErrorComponent
        | ApiV1IncidentsArchiveCreateArchivedReasonErrorComponent
        | ApiV1IncidentsArchiveCreateCreatedByComponentErrorComponent
        | ApiV1IncidentsArchiveCreateCreatedByUserErrorComponent
        | ApiV1IncidentsArchiveCreateCriticalityErrorComponent
        | ApiV1IncidentsArchiveCreateDebugModeErrorComponent
        | ApiV1IncidentsArchiveCreateDiscoveredAtErrorComponent
        | ApiV1IncidentsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1IncidentsArchiveCreateDisplayNameErrorComponent
        | ApiV1IncidentsArchiveCreateDowntimeIdsErrorComponent
        | ApiV1IncidentsArchiveCreateKindErrorComponent
        | ApiV1IncidentsArchiveCreateLabelsErrorComponent
        | ApiV1IncidentsArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1IncidentsArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1IncidentsArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1IncidentsArchiveCreateModifiedByUserErrorComponent
        | ApiV1IncidentsArchiveCreateNameErrorComponent
        | ApiV1IncidentsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1IncidentsArchiveCreateNotificationClosedSentErrorComponent
        | ApiV1IncidentsArchiveCreateNotificationOpenedSentErrorComponent
        | ApiV1IncidentsArchiveCreateOccurredAtErrorComponent
        | ApiV1IncidentsArchiveCreateOrganizationIdErrorComponent
        | ApiV1IncidentsArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1IncidentsArchiveCreatePlatformServiceErrorComponent
        | ApiV1IncidentsArchiveCreateProviderEntityErrorComponent
        | ApiV1IncidentsArchiveCreateProviderErrorComponent
        | ApiV1IncidentsArchiveCreateProviderIdErrorComponent
        | ApiV1IncidentsArchiveCreateProviderReferenceErrorComponent
        | ApiV1IncidentsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1IncidentsArchiveCreateReferenceUrlErrorComponent
        | ApiV1IncidentsArchiveCreateReporterErrorComponent
        | ApiV1IncidentsArchiveCreateResolvedAtErrorComponent
        | ApiV1IncidentsArchiveCreateScopeErrorComponent
        | ApiV1IncidentsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1IncidentsArchiveCreateSlaTargetErrorComponent
        | ApiV1IncidentsArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1IncidentsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1IncidentsArchiveCreateSloTargetErrorComponent
        | ApiV1IncidentsArchiveCreateSloWindowDaysErrorComponent
        | ApiV1IncidentsArchiveCreateSourceDatasourceErrorComponent
        | ApiV1IncidentsArchiveCreateSourceItemIdErrorComponent
        | ApiV1IncidentsArchiveCreateStatusErrorComponent
        | ApiV1IncidentsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1IncidentsArchiveCreateVulnerabilityFindingIdsErrorComponent
        | ApiV1IncidentsArchiveCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_incidents_archive_create_actual_availability_error_component import (
            ApiV1IncidentsArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_affected_host_ids_error_component import (
            ApiV1IncidentsArchiveCreateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_affected_pop_ids_error_component import (
            ApiV1IncidentsArchiveCreateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_affected_volume_ids_error_component import (
            ApiV1IncidentsArchiveCreateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_annotations_error_component import (
            ApiV1IncidentsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_archived_at_error_component import (
            ApiV1IncidentsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_archived_by_error_component import (
            ApiV1IncidentsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_archived_error_component import (
            ApiV1IncidentsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_archived_reason_error_component import (
            ApiV1IncidentsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_created_by_component_error_component import (
            ApiV1IncidentsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_created_by_user_error_component import (
            ApiV1IncidentsArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_criticality_error_component import (
            ApiV1IncidentsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_debug_mode_error_component import (
            ApiV1IncidentsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_discovered_at_error_component import (
            ApiV1IncidentsArchiveCreateDiscoveredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_discovery_enabled_error_component import (
            ApiV1IncidentsArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_display_name_error_component import (
            ApiV1IncidentsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_downtime_ids_error_component import (
            ApiV1IncidentsArchiveCreateDowntimeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_kind_error_component import (
            ApiV1IncidentsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_labels_error_component import (
            ApiV1IncidentsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1IncidentsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_managed_by_content_type_error_component import (
            ApiV1IncidentsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_managed_by_object_id_error_component import (
            ApiV1IncidentsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_modified_by_user_error_component import (
            ApiV1IncidentsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_name_error_component import (
            ApiV1IncidentsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_non_field_errors_error_component import (
            ApiV1IncidentsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_notification_closed_sent_error_component import (
            ApiV1IncidentsArchiveCreateNotificationClosedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_notification_opened_sent_error_component import (
            ApiV1IncidentsArchiveCreateNotificationOpenedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_occurred_at_error_component import (
            ApiV1IncidentsArchiveCreateOccurredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_organization_id_error_component import (
            ApiV1IncidentsArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_platform_dns_record_created_error_component import (
            ApiV1IncidentsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_platform_service_error_component import (
            ApiV1IncidentsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_provider_entity_error_component import (
            ApiV1IncidentsArchiveCreateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_provider_error_component import (
            ApiV1IncidentsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_provider_id_error_component import (
            ApiV1IncidentsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_provider_reference_error_component import (
            ApiV1IncidentsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_reconciliation_enabled_error_component import (
            ApiV1IncidentsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_reference_url_error_component import (
            ApiV1IncidentsArchiveCreateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_reporter_error_component import (
            ApiV1IncidentsArchiveCreateReporterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_resolved_at_error_component import (
            ApiV1IncidentsArchiveCreateResolvedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_scope_error_component import (
            ApiV1IncidentsArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_sla_availability_error_component import (
            ApiV1IncidentsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_sla_target_error_component import (
            ApiV1IncidentsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_sla_window_days_error_component import (
            ApiV1IncidentsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_slo_availability_error_component import (
            ApiV1IncidentsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_slo_target_error_component import (
            ApiV1IncidentsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_slo_window_days_error_component import (
            ApiV1IncidentsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_source_item_id_error_component import (
            ApiV1IncidentsArchiveCreateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_status_error_component import (
            ApiV1IncidentsArchiveCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_target_availability_error_component import (
            ApiV1IncidentsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_vulnerability_finding_ids_error_component import (
            ApiV1IncidentsArchiveCreateVulnerabilityFindingIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_workspace_id_error_component import (
            ApiV1IncidentsArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IncidentsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateDowntimeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateAffectedHostIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateAffectedVolumeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateAffectedPopIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateVulnerabilityFindingIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1IncidentsArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateOccurredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateDiscoveredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateResolvedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateReporterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateReferenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateSourceItemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateNotificationOpenedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateNotificationClosedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsArchiveCreateProviderEntityErrorComponent):
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
        from ..models.api_v1_incidents_archive_create_actual_availability_error_component import (
            ApiV1IncidentsArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_affected_host_ids_error_component import (
            ApiV1IncidentsArchiveCreateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_affected_pop_ids_error_component import (
            ApiV1IncidentsArchiveCreateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_affected_volume_ids_error_component import (
            ApiV1IncidentsArchiveCreateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_annotations_error_component import (
            ApiV1IncidentsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_archived_at_error_component import (
            ApiV1IncidentsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_archived_by_error_component import (
            ApiV1IncidentsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_archived_error_component import (
            ApiV1IncidentsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_archived_reason_error_component import (
            ApiV1IncidentsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_created_by_component_error_component import (
            ApiV1IncidentsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_created_by_user_error_component import (
            ApiV1IncidentsArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_criticality_error_component import (
            ApiV1IncidentsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_debug_mode_error_component import (
            ApiV1IncidentsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_discovered_at_error_component import (
            ApiV1IncidentsArchiveCreateDiscoveredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_discovery_enabled_error_component import (
            ApiV1IncidentsArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_display_name_error_component import (
            ApiV1IncidentsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_downtime_ids_error_component import (
            ApiV1IncidentsArchiveCreateDowntimeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_kind_error_component import (
            ApiV1IncidentsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_labels_error_component import (
            ApiV1IncidentsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1IncidentsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_managed_by_content_type_error_component import (
            ApiV1IncidentsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_managed_by_object_id_error_component import (
            ApiV1IncidentsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_modified_by_user_error_component import (
            ApiV1IncidentsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_name_error_component import (
            ApiV1IncidentsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_non_field_errors_error_component import (
            ApiV1IncidentsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_notification_closed_sent_error_component import (
            ApiV1IncidentsArchiveCreateNotificationClosedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_notification_opened_sent_error_component import (
            ApiV1IncidentsArchiveCreateNotificationOpenedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_occurred_at_error_component import (
            ApiV1IncidentsArchiveCreateOccurredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_organization_id_error_component import (
            ApiV1IncidentsArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_platform_dns_record_created_error_component import (
            ApiV1IncidentsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_platform_service_error_component import (
            ApiV1IncidentsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_provider_entity_error_component import (
            ApiV1IncidentsArchiveCreateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_provider_error_component import (
            ApiV1IncidentsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_provider_id_error_component import (
            ApiV1IncidentsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_provider_reference_error_component import (
            ApiV1IncidentsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_reconciliation_enabled_error_component import (
            ApiV1IncidentsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_reference_url_error_component import (
            ApiV1IncidentsArchiveCreateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_reporter_error_component import (
            ApiV1IncidentsArchiveCreateReporterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_resolved_at_error_component import (
            ApiV1IncidentsArchiveCreateResolvedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_scope_error_component import (
            ApiV1IncidentsArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_sla_availability_error_component import (
            ApiV1IncidentsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_sla_target_error_component import (
            ApiV1IncidentsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_sla_window_days_error_component import (
            ApiV1IncidentsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_slo_availability_error_component import (
            ApiV1IncidentsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_slo_target_error_component import (
            ApiV1IncidentsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_slo_window_days_error_component import (
            ApiV1IncidentsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_source_datasource_error_component import (
            ApiV1IncidentsArchiveCreateSourceDatasourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_source_item_id_error_component import (
            ApiV1IncidentsArchiveCreateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_status_error_component import (
            ApiV1IncidentsArchiveCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_target_availability_error_component import (
            ApiV1IncidentsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_vulnerability_finding_ids_error_component import (
            ApiV1IncidentsArchiveCreateVulnerabilityFindingIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_archive_create_workspace_id_error_component import (
            ApiV1IncidentsArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IncidentsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1IncidentsArchiveCreateAffectedHostIdsErrorComponent
                | ApiV1IncidentsArchiveCreateAffectedPopIdsErrorComponent
                | ApiV1IncidentsArchiveCreateAffectedVolumeIdsErrorComponent
                | ApiV1IncidentsArchiveCreateAnnotationsErrorComponent
                | ApiV1IncidentsArchiveCreateArchivedAtErrorComponent
                | ApiV1IncidentsArchiveCreateArchivedByErrorComponent
                | ApiV1IncidentsArchiveCreateArchivedErrorComponent
                | ApiV1IncidentsArchiveCreateArchivedReasonErrorComponent
                | ApiV1IncidentsArchiveCreateCreatedByComponentErrorComponent
                | ApiV1IncidentsArchiveCreateCreatedByUserErrorComponent
                | ApiV1IncidentsArchiveCreateCriticalityErrorComponent
                | ApiV1IncidentsArchiveCreateDebugModeErrorComponent
                | ApiV1IncidentsArchiveCreateDiscoveredAtErrorComponent
                | ApiV1IncidentsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1IncidentsArchiveCreateDisplayNameErrorComponent
                | ApiV1IncidentsArchiveCreateDowntimeIdsErrorComponent
                | ApiV1IncidentsArchiveCreateKindErrorComponent
                | ApiV1IncidentsArchiveCreateLabelsErrorComponent
                | ApiV1IncidentsArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1IncidentsArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1IncidentsArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1IncidentsArchiveCreateModifiedByUserErrorComponent
                | ApiV1IncidentsArchiveCreateNameErrorComponent
                | ApiV1IncidentsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1IncidentsArchiveCreateNotificationClosedSentErrorComponent
                | ApiV1IncidentsArchiveCreateNotificationOpenedSentErrorComponent
                | ApiV1IncidentsArchiveCreateOccurredAtErrorComponent
                | ApiV1IncidentsArchiveCreateOrganizationIdErrorComponent
                | ApiV1IncidentsArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1IncidentsArchiveCreatePlatformServiceErrorComponent
                | ApiV1IncidentsArchiveCreateProviderEntityErrorComponent
                | ApiV1IncidentsArchiveCreateProviderErrorComponent
                | ApiV1IncidentsArchiveCreateProviderIdErrorComponent
                | ApiV1IncidentsArchiveCreateProviderReferenceErrorComponent
                | ApiV1IncidentsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1IncidentsArchiveCreateReferenceUrlErrorComponent
                | ApiV1IncidentsArchiveCreateReporterErrorComponent
                | ApiV1IncidentsArchiveCreateResolvedAtErrorComponent
                | ApiV1IncidentsArchiveCreateScopeErrorComponent
                | ApiV1IncidentsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1IncidentsArchiveCreateSlaTargetErrorComponent
                | ApiV1IncidentsArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1IncidentsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1IncidentsArchiveCreateSloTargetErrorComponent
                | ApiV1IncidentsArchiveCreateSloWindowDaysErrorComponent
                | ApiV1IncidentsArchiveCreateSourceDatasourceErrorComponent
                | ApiV1IncidentsArchiveCreateSourceItemIdErrorComponent
                | ApiV1IncidentsArchiveCreateStatusErrorComponent
                | ApiV1IncidentsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1IncidentsArchiveCreateVulnerabilityFindingIdsErrorComponent
                | ApiV1IncidentsArchiveCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_0 = (
                        ApiV1IncidentsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_1 = (
                        ApiV1IncidentsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_2 = (
                        ApiV1IncidentsArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_3 = (
                        ApiV1IncidentsArchiveCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_4 = (
                        ApiV1IncidentsArchiveCreateDowntimeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_5 = (
                        ApiV1IncidentsArchiveCreateAffectedHostIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_6 = (
                        ApiV1IncidentsArchiveCreateAffectedVolumeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_7 = (
                        ApiV1IncidentsArchiveCreateAffectedPopIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_8 = (
                        ApiV1IncidentsArchiveCreateVulnerabilityFindingIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_9 = (
                        ApiV1IncidentsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_10 = (
                        ApiV1IncidentsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_11 = (
                        ApiV1IncidentsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_12 = (
                        ApiV1IncidentsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_13 = (
                        ApiV1IncidentsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_14 = (
                        ApiV1IncidentsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_15 = (
                        ApiV1IncidentsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_16 = (
                        ApiV1IncidentsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_17 = (
                        ApiV1IncidentsArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_18 = (
                        ApiV1IncidentsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_19 = (
                        ApiV1IncidentsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_20 = (
                        ApiV1IncidentsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_21 = (
                        ApiV1IncidentsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_22 = (
                        ApiV1IncidentsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_23 = (
                        ApiV1IncidentsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_24 = (
                        ApiV1IncidentsArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_25 = (
                        ApiV1IncidentsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_26 = (
                        ApiV1IncidentsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_27 = (
                        ApiV1IncidentsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_28 = (
                        ApiV1IncidentsArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_29 = (
                        ApiV1IncidentsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_30 = (
                        ApiV1IncidentsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_31 = (
                        ApiV1IncidentsArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_32 = (
                        ApiV1IncidentsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_33 = (
                        ApiV1IncidentsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_34 = (
                        ApiV1IncidentsArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_35 = (
                        ApiV1IncidentsArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_36 = (
                        ApiV1IncidentsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_37 = (
                        ApiV1IncidentsArchiveCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_38 = (
                        ApiV1IncidentsArchiveCreateOccurredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_39 = (
                        ApiV1IncidentsArchiveCreateDiscoveredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_40 = (
                        ApiV1IncidentsArchiveCreateResolvedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_41 = (
                        ApiV1IncidentsArchiveCreateReporterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_42 = (
                        ApiV1IncidentsArchiveCreateReferenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_43 = (
                        ApiV1IncidentsArchiveCreateSourceItemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_44 = (
                        ApiV1IncidentsArchiveCreateNotificationOpenedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_45 = (
                        ApiV1IncidentsArchiveCreateNotificationClosedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_46 = (
                        ApiV1IncidentsArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_47 = (
                        ApiV1IncidentsArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_48 = (
                        ApiV1IncidentsArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_49 = (
                        ApiV1IncidentsArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_archive_create_error_type_50 = (
                        ApiV1IncidentsArchiveCreateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_archive_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_incidents_archive_create_error_type_51 = (
                    ApiV1IncidentsArchiveCreateSourceDatasourceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_incidents_archive_create_error_type_51

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_incidents_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_incidents_archive_create_validation_error.additional_properties = d
        return api_v1_incidents_archive_create_validation_error

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
