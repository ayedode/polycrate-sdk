from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_datasources_archive_create_annotations_error_component import (
        ApiV1DatasourcesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_archived_at_error_component import (
        ApiV1DatasourcesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_archived_error_component import (
        ApiV1DatasourcesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_archived_reason_error_component import (
        ApiV1DatasourcesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_create_incidents_error_component import (
        ApiV1DatasourcesArchiveCreateCreateIncidentsErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_create_incidents_without_resources_error_component import (
        ApiV1DatasourcesArchiveCreateCreateIncidentsWithoutResourcesErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_create_maintenance_as_draft_error_component import (
        ApiV1DatasourcesArchiveCreateCreateMaintenanceAsDraftErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_create_notes_resolved_error_component import (
        ApiV1DatasourcesArchiveCreateCreateNotesResolvedErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_criticality_error_component import (
        ApiV1DatasourcesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_datasource_url_error_component import (
        ApiV1DatasourcesArchiveCreateDatasourceUrlErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_debug_mode_error_component import (
        ApiV1DatasourcesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_display_name_error_component import (
        ApiV1DatasourcesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_is_enabled_error_component import (
        ApiV1DatasourcesArchiveCreateIsEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_kind_error_component import (
        ApiV1DatasourcesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_labels_error_component import (
        ApiV1DatasourcesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_last_sync_error_component import (
        ApiV1DatasourcesArchiveCreateLastSyncErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_last_sync_error_error_component import (
        ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_name_error_component import (
        ApiV1DatasourcesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_non_field_errors_error_component import (
        ApiV1DatasourcesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_note_kind_error_component import (
        ApiV1DatasourcesArchiveCreateNoteKindErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_note_organization_id_error_component import (
        ApiV1DatasourcesArchiveCreateNoteOrganizationIdErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_note_workspace_id_error_component import (
        ApiV1DatasourcesArchiveCreateNoteWorkspaceIdErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_platform_service_error_component import (
        ApiV1DatasourcesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_provider_entity_id_error_component import (
        ApiV1DatasourcesArchiveCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_provider_error_component import (
        ApiV1DatasourcesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_provider_id_error_component import (
        ApiV1DatasourcesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_provider_reference_error_component import (
        ApiV1DatasourcesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_reconciliation_enabled_error_component import (
        ApiV1DatasourcesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_sla_availability_error_component import (
        ApiV1DatasourcesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_sla_target_error_component import (
        ApiV1DatasourcesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_slo_availability_error_component import (
        ApiV1DatasourcesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_slo_target_error_component import (
        ApiV1DatasourcesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_sync_interval_minutes_error_component import (
        ApiV1DatasourcesArchiveCreateSyncIntervalMinutesErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_target_availability_error_component import (
        ApiV1DatasourcesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_archive_create_tolerations_error_component import (
        ApiV1DatasourcesArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DatasourcesArchiveCreateValidationError")


@_attrs_define
class ApiV1DatasourcesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DatasourcesArchiveCreateAnnotationsErrorComponent |
            ApiV1DatasourcesArchiveCreateArchivedAtErrorComponent | ApiV1DatasourcesArchiveCreateArchivedErrorComponent |
            ApiV1DatasourcesArchiveCreateArchivedReasonErrorComponent |
            ApiV1DatasourcesArchiveCreateCreateIncidentsErrorComponent |
            ApiV1DatasourcesArchiveCreateCreateIncidentsWithoutResourcesErrorComponent |
            ApiV1DatasourcesArchiveCreateCreateMaintenanceAsDraftErrorComponent |
            ApiV1DatasourcesArchiveCreateCreateNotesResolvedErrorComponent |
            ApiV1DatasourcesArchiveCreateCriticalityErrorComponent |
            ApiV1DatasourcesArchiveCreateDatasourceUrlErrorComponent | ApiV1DatasourcesArchiveCreateDebugModeErrorComponent
            | ApiV1DatasourcesArchiveCreateDisplayNameErrorComponent | ApiV1DatasourcesArchiveCreateIsEnabledErrorComponent
            | ApiV1DatasourcesArchiveCreateKindErrorComponent | ApiV1DatasourcesArchiveCreateLabelsErrorComponent |
            ApiV1DatasourcesArchiveCreateLastSyncErrorComponent | ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponent |
            ApiV1DatasourcesArchiveCreateNameErrorComponent | ApiV1DatasourcesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1DatasourcesArchiveCreateNoteKindErrorComponent |
            ApiV1DatasourcesArchiveCreateNoteOrganizationIdErrorComponent |
            ApiV1DatasourcesArchiveCreateNoteWorkspaceIdErrorComponent |
            ApiV1DatasourcesArchiveCreatePlatformServiceErrorComponent |
            ApiV1DatasourcesArchiveCreateProviderEntityIdErrorComponent |
            ApiV1DatasourcesArchiveCreateProviderErrorComponent | ApiV1DatasourcesArchiveCreateProviderIdErrorComponent |
            ApiV1DatasourcesArchiveCreateProviderReferenceErrorComponent |
            ApiV1DatasourcesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1DatasourcesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1DatasourcesArchiveCreateSlaTargetErrorComponent |
            ApiV1DatasourcesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1DatasourcesArchiveCreateSloTargetErrorComponent |
            ApiV1DatasourcesArchiveCreateSyncIntervalMinutesErrorComponent |
            ApiV1DatasourcesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1DatasourcesArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DatasourcesArchiveCreateAnnotationsErrorComponent
        | ApiV1DatasourcesArchiveCreateArchivedAtErrorComponent
        | ApiV1DatasourcesArchiveCreateArchivedErrorComponent
        | ApiV1DatasourcesArchiveCreateArchivedReasonErrorComponent
        | ApiV1DatasourcesArchiveCreateCreateIncidentsErrorComponent
        | ApiV1DatasourcesArchiveCreateCreateIncidentsWithoutResourcesErrorComponent
        | ApiV1DatasourcesArchiveCreateCreateMaintenanceAsDraftErrorComponent
        | ApiV1DatasourcesArchiveCreateCreateNotesResolvedErrorComponent
        | ApiV1DatasourcesArchiveCreateCriticalityErrorComponent
        | ApiV1DatasourcesArchiveCreateDatasourceUrlErrorComponent
        | ApiV1DatasourcesArchiveCreateDebugModeErrorComponent
        | ApiV1DatasourcesArchiveCreateDisplayNameErrorComponent
        | ApiV1DatasourcesArchiveCreateIsEnabledErrorComponent
        | ApiV1DatasourcesArchiveCreateKindErrorComponent
        | ApiV1DatasourcesArchiveCreateLabelsErrorComponent
        | ApiV1DatasourcesArchiveCreateLastSyncErrorComponent
        | ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponent
        | ApiV1DatasourcesArchiveCreateNameErrorComponent
        | ApiV1DatasourcesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1DatasourcesArchiveCreateNoteKindErrorComponent
        | ApiV1DatasourcesArchiveCreateNoteOrganizationIdErrorComponent
        | ApiV1DatasourcesArchiveCreateNoteWorkspaceIdErrorComponent
        | ApiV1DatasourcesArchiveCreatePlatformServiceErrorComponent
        | ApiV1DatasourcesArchiveCreateProviderEntityIdErrorComponent
        | ApiV1DatasourcesArchiveCreateProviderErrorComponent
        | ApiV1DatasourcesArchiveCreateProviderIdErrorComponent
        | ApiV1DatasourcesArchiveCreateProviderReferenceErrorComponent
        | ApiV1DatasourcesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1DatasourcesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1DatasourcesArchiveCreateSlaTargetErrorComponent
        | ApiV1DatasourcesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1DatasourcesArchiveCreateSloTargetErrorComponent
        | ApiV1DatasourcesArchiveCreateSyncIntervalMinutesErrorComponent
        | ApiV1DatasourcesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1DatasourcesArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_datasources_archive_create_annotations_error_component import (
            ApiV1DatasourcesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_archived_at_error_component import (
            ApiV1DatasourcesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_archived_error_component import (
            ApiV1DatasourcesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_archived_reason_error_component import (
            ApiV1DatasourcesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_create_incidents_error_component import (
            ApiV1DatasourcesArchiveCreateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesArchiveCreateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesArchiveCreateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_create_notes_resolved_error_component import (
            ApiV1DatasourcesArchiveCreateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_criticality_error_component import (
            ApiV1DatasourcesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_datasource_url_error_component import (
            ApiV1DatasourcesArchiveCreateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_debug_mode_error_component import (
            ApiV1DatasourcesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_display_name_error_component import (
            ApiV1DatasourcesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_is_enabled_error_component import (
            ApiV1DatasourcesArchiveCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_kind_error_component import (
            ApiV1DatasourcesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_labels_error_component import (
            ApiV1DatasourcesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_last_sync_error_component import (
            ApiV1DatasourcesArchiveCreateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_last_sync_error_error_component import (
            ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_name_error_component import (
            ApiV1DatasourcesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_non_field_errors_error_component import (
            ApiV1DatasourcesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_note_kind_error_component import (
            ApiV1DatasourcesArchiveCreateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_note_organization_id_error_component import (
            ApiV1DatasourcesArchiveCreateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_note_workspace_id_error_component import (
            ApiV1DatasourcesArchiveCreateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_platform_service_error_component import (
            ApiV1DatasourcesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_provider_error_component import (
            ApiV1DatasourcesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_provider_id_error_component import (
            ApiV1DatasourcesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_provider_reference_error_component import (
            ApiV1DatasourcesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_reconciliation_enabled_error_component import (
            ApiV1DatasourcesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_sla_availability_error_component import (
            ApiV1DatasourcesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_sla_target_error_component import (
            ApiV1DatasourcesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_slo_availability_error_component import (
            ApiV1DatasourcesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_slo_target_error_component import (
            ApiV1DatasourcesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_sync_interval_minutes_error_component import (
            ApiV1DatasourcesArchiveCreateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_target_availability_error_component import (
            ApiV1DatasourcesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_tolerations_error_component import (
            ApiV1DatasourcesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateDatasourceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateSyncIntervalMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateNoteKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateNoteOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateNoteWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateCreateNotesResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateCreateMaintenanceAsDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateCreateIncidentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DatasourcesArchiveCreateCreateIncidentsWithoutResourcesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateLastSyncErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponent):
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
        from ..models.api_v1_datasources_archive_create_annotations_error_component import (
            ApiV1DatasourcesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_archived_at_error_component import (
            ApiV1DatasourcesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_archived_error_component import (
            ApiV1DatasourcesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_archived_reason_error_component import (
            ApiV1DatasourcesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_create_incidents_error_component import (
            ApiV1DatasourcesArchiveCreateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesArchiveCreateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesArchiveCreateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_create_notes_resolved_error_component import (
            ApiV1DatasourcesArchiveCreateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_criticality_error_component import (
            ApiV1DatasourcesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_datasource_url_error_component import (
            ApiV1DatasourcesArchiveCreateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_debug_mode_error_component import (
            ApiV1DatasourcesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_display_name_error_component import (
            ApiV1DatasourcesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_is_enabled_error_component import (
            ApiV1DatasourcesArchiveCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_kind_error_component import (
            ApiV1DatasourcesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_labels_error_component import (
            ApiV1DatasourcesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_last_sync_error_component import (
            ApiV1DatasourcesArchiveCreateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_last_sync_error_error_component import (
            ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_name_error_component import (
            ApiV1DatasourcesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_non_field_errors_error_component import (
            ApiV1DatasourcesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_note_kind_error_component import (
            ApiV1DatasourcesArchiveCreateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_note_organization_id_error_component import (
            ApiV1DatasourcesArchiveCreateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_note_workspace_id_error_component import (
            ApiV1DatasourcesArchiveCreateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_platform_service_error_component import (
            ApiV1DatasourcesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_provider_entity_id_error_component import (
            ApiV1DatasourcesArchiveCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_provider_error_component import (
            ApiV1DatasourcesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_provider_id_error_component import (
            ApiV1DatasourcesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_provider_reference_error_component import (
            ApiV1DatasourcesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_reconciliation_enabled_error_component import (
            ApiV1DatasourcesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_sla_availability_error_component import (
            ApiV1DatasourcesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_sla_target_error_component import (
            ApiV1DatasourcesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_slo_availability_error_component import (
            ApiV1DatasourcesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_slo_target_error_component import (
            ApiV1DatasourcesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_sync_interval_minutes_error_component import (
            ApiV1DatasourcesArchiveCreateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_target_availability_error_component import (
            ApiV1DatasourcesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_archive_create_tolerations_error_component import (
            ApiV1DatasourcesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DatasourcesArchiveCreateAnnotationsErrorComponent
                | ApiV1DatasourcesArchiveCreateArchivedAtErrorComponent
                | ApiV1DatasourcesArchiveCreateArchivedErrorComponent
                | ApiV1DatasourcesArchiveCreateArchivedReasonErrorComponent
                | ApiV1DatasourcesArchiveCreateCreateIncidentsErrorComponent
                | ApiV1DatasourcesArchiveCreateCreateIncidentsWithoutResourcesErrorComponent
                | ApiV1DatasourcesArchiveCreateCreateMaintenanceAsDraftErrorComponent
                | ApiV1DatasourcesArchiveCreateCreateNotesResolvedErrorComponent
                | ApiV1DatasourcesArchiveCreateCriticalityErrorComponent
                | ApiV1DatasourcesArchiveCreateDatasourceUrlErrorComponent
                | ApiV1DatasourcesArchiveCreateDebugModeErrorComponent
                | ApiV1DatasourcesArchiveCreateDisplayNameErrorComponent
                | ApiV1DatasourcesArchiveCreateIsEnabledErrorComponent
                | ApiV1DatasourcesArchiveCreateKindErrorComponent
                | ApiV1DatasourcesArchiveCreateLabelsErrorComponent
                | ApiV1DatasourcesArchiveCreateLastSyncErrorComponent
                | ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponent
                | ApiV1DatasourcesArchiveCreateNameErrorComponent
                | ApiV1DatasourcesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1DatasourcesArchiveCreateNoteKindErrorComponent
                | ApiV1DatasourcesArchiveCreateNoteOrganizationIdErrorComponent
                | ApiV1DatasourcesArchiveCreateNoteWorkspaceIdErrorComponent
                | ApiV1DatasourcesArchiveCreatePlatformServiceErrorComponent
                | ApiV1DatasourcesArchiveCreateProviderEntityIdErrorComponent
                | ApiV1DatasourcesArchiveCreateProviderErrorComponent
                | ApiV1DatasourcesArchiveCreateProviderIdErrorComponent
                | ApiV1DatasourcesArchiveCreateProviderReferenceErrorComponent
                | ApiV1DatasourcesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1DatasourcesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1DatasourcesArchiveCreateSlaTargetErrorComponent
                | ApiV1DatasourcesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1DatasourcesArchiveCreateSloTargetErrorComponent
                | ApiV1DatasourcesArchiveCreateSyncIntervalMinutesErrorComponent
                | ApiV1DatasourcesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1DatasourcesArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_0 = (
                        ApiV1DatasourcesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_1 = (
                        ApiV1DatasourcesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_2 = (
                        ApiV1DatasourcesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_3 = (
                        ApiV1DatasourcesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_4 = (
                        ApiV1DatasourcesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_5 = (
                        ApiV1DatasourcesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_6 = (
                        ApiV1DatasourcesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_7 = (
                        ApiV1DatasourcesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_8 = (
                        ApiV1DatasourcesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_9 = (
                        ApiV1DatasourcesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_10 = (
                        ApiV1DatasourcesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_11 = (
                        ApiV1DatasourcesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_12 = (
                        ApiV1DatasourcesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_13 = (
                        ApiV1DatasourcesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_14 = (
                        ApiV1DatasourcesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_15 = (
                        ApiV1DatasourcesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_16 = (
                        ApiV1DatasourcesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_17 = (
                        ApiV1DatasourcesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_18 = (
                        ApiV1DatasourcesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_19 = (
                        ApiV1DatasourcesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_20 = (
                        ApiV1DatasourcesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_21 = (
                        ApiV1DatasourcesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_22 = (
                        ApiV1DatasourcesArchiveCreateDatasourceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_23 = (
                        ApiV1DatasourcesArchiveCreateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_24 = (
                        ApiV1DatasourcesArchiveCreateSyncIntervalMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_25 = (
                        ApiV1DatasourcesArchiveCreateNoteKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_26 = (
                        ApiV1DatasourcesArchiveCreateNoteOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_27 = (
                        ApiV1DatasourcesArchiveCreateNoteWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_28 = (
                        ApiV1DatasourcesArchiveCreateCreateNotesResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_29 = (
                        ApiV1DatasourcesArchiveCreateCreateMaintenanceAsDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_30 = (
                        ApiV1DatasourcesArchiveCreateCreateIncidentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_31 = (
                        ApiV1DatasourcesArchiveCreateCreateIncidentsWithoutResourcesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_32 = (
                        ApiV1DatasourcesArchiveCreateLastSyncErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_archive_create_error_type_33 = (
                        ApiV1DatasourcesArchiveCreateLastSyncErrorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_datasources_archive_create_error_type_34 = (
                    ApiV1DatasourcesArchiveCreateProviderEntityIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_datasources_archive_create_error_type_34

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_datasources_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_datasources_archive_create_validation_error.additional_properties = d
        return api_v1_datasources_archive_create_validation_error

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
