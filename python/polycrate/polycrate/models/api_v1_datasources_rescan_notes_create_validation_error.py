from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_datasources_rescan_notes_create_annotations_error_component import (
        ApiV1DatasourcesRescanNotesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_archived_at_error_component import (
        ApiV1DatasourcesRescanNotesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_archived_error_component import (
        ApiV1DatasourcesRescanNotesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_archived_reason_error_component import (
        ApiV1DatasourcesRescanNotesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_create_incidents_error_component import (
        ApiV1DatasourcesRescanNotesCreateCreateIncidentsErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_create_incidents_without_resources_error_component import (
        ApiV1DatasourcesRescanNotesCreateCreateIncidentsWithoutResourcesErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_create_maintenance_as_draft_error_component import (
        ApiV1DatasourcesRescanNotesCreateCreateMaintenanceAsDraftErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_create_notes_resolved_error_component import (
        ApiV1DatasourcesRescanNotesCreateCreateNotesResolvedErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_criticality_error_component import (
        ApiV1DatasourcesRescanNotesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_datasource_url_error_component import (
        ApiV1DatasourcesRescanNotesCreateDatasourceUrlErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_debug_mode_error_component import (
        ApiV1DatasourcesRescanNotesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_display_name_error_component import (
        ApiV1DatasourcesRescanNotesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_is_enabled_error_component import (
        ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_kind_error_component import (
        ApiV1DatasourcesRescanNotesCreateKindErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_labels_error_component import (
        ApiV1DatasourcesRescanNotesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_last_sync_error_component import (
        ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_last_sync_error_error_component import (
        ApiV1DatasourcesRescanNotesCreateLastSyncErrorErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_name_error_component import (
        ApiV1DatasourcesRescanNotesCreateNameErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_non_field_errors_error_component import (
        ApiV1DatasourcesRescanNotesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_note_kind_error_component import (
        ApiV1DatasourcesRescanNotesCreateNoteKindErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_note_organization_id_error_component import (
        ApiV1DatasourcesRescanNotesCreateNoteOrganizationIdErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_note_workspace_id_error_component import (
        ApiV1DatasourcesRescanNotesCreateNoteWorkspaceIdErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_platform_service_error_component import (
        ApiV1DatasourcesRescanNotesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_provider_entity_id_error_component import (
        ApiV1DatasourcesRescanNotesCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_provider_error_component import (
        ApiV1DatasourcesRescanNotesCreateProviderErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_provider_id_error_component import (
        ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_provider_reference_error_component import (
        ApiV1DatasourcesRescanNotesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_reconciliation_enabled_error_component import (
        ApiV1DatasourcesRescanNotesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_sla_availability_error_component import (
        ApiV1DatasourcesRescanNotesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_sla_target_error_component import (
        ApiV1DatasourcesRescanNotesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_slo_availability_error_component import (
        ApiV1DatasourcesRescanNotesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_slo_target_error_component import (
        ApiV1DatasourcesRescanNotesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_sync_interval_minutes_error_component import (
        ApiV1DatasourcesRescanNotesCreateSyncIntervalMinutesErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_target_availability_error_component import (
        ApiV1DatasourcesRescanNotesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_rescan_notes_create_tolerations_error_component import (
        ApiV1DatasourcesRescanNotesCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DatasourcesRescanNotesCreateValidationError")


@_attrs_define
class ApiV1DatasourcesRescanNotesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DatasourcesRescanNotesCreateAnnotationsErrorComponent |
            ApiV1DatasourcesRescanNotesCreateArchivedAtErrorComponent |
            ApiV1DatasourcesRescanNotesCreateArchivedErrorComponent |
            ApiV1DatasourcesRescanNotesCreateArchivedReasonErrorComponent |
            ApiV1DatasourcesRescanNotesCreateCreateIncidentsErrorComponent |
            ApiV1DatasourcesRescanNotesCreateCreateIncidentsWithoutResourcesErrorComponent |
            ApiV1DatasourcesRescanNotesCreateCreateMaintenanceAsDraftErrorComponent |
            ApiV1DatasourcesRescanNotesCreateCreateNotesResolvedErrorComponent |
            ApiV1DatasourcesRescanNotesCreateCriticalityErrorComponent |
            ApiV1DatasourcesRescanNotesCreateDatasourceUrlErrorComponent |
            ApiV1DatasourcesRescanNotesCreateDebugModeErrorComponent |
            ApiV1DatasourcesRescanNotesCreateDisplayNameErrorComponent |
            ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponent | ApiV1DatasourcesRescanNotesCreateKindErrorComponent |
            ApiV1DatasourcesRescanNotesCreateLabelsErrorComponent | ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponent
            | ApiV1DatasourcesRescanNotesCreateLastSyncErrorErrorComponent |
            ApiV1DatasourcesRescanNotesCreateNameErrorComponent |
            ApiV1DatasourcesRescanNotesCreateNonFieldErrorsErrorComponent |
            ApiV1DatasourcesRescanNotesCreateNoteKindErrorComponent |
            ApiV1DatasourcesRescanNotesCreateNoteOrganizationIdErrorComponent |
            ApiV1DatasourcesRescanNotesCreateNoteWorkspaceIdErrorComponent |
            ApiV1DatasourcesRescanNotesCreatePlatformServiceErrorComponent |
            ApiV1DatasourcesRescanNotesCreateProviderEntityIdErrorComponent |
            ApiV1DatasourcesRescanNotesCreateProviderErrorComponent |
            ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponent |
            ApiV1DatasourcesRescanNotesCreateProviderReferenceErrorComponent |
            ApiV1DatasourcesRescanNotesCreateReconciliationEnabledErrorComponent |
            ApiV1DatasourcesRescanNotesCreateSlaAvailabilityErrorComponent |
            ApiV1DatasourcesRescanNotesCreateSlaTargetErrorComponent |
            ApiV1DatasourcesRescanNotesCreateSloAvailabilityErrorComponent |
            ApiV1DatasourcesRescanNotesCreateSloTargetErrorComponent |
            ApiV1DatasourcesRescanNotesCreateSyncIntervalMinutesErrorComponent |
            ApiV1DatasourcesRescanNotesCreateTargetAvailabilityErrorComponent |
            ApiV1DatasourcesRescanNotesCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DatasourcesRescanNotesCreateAnnotationsErrorComponent
        | ApiV1DatasourcesRescanNotesCreateArchivedAtErrorComponent
        | ApiV1DatasourcesRescanNotesCreateArchivedErrorComponent
        | ApiV1DatasourcesRescanNotesCreateArchivedReasonErrorComponent
        | ApiV1DatasourcesRescanNotesCreateCreateIncidentsErrorComponent
        | ApiV1DatasourcesRescanNotesCreateCreateIncidentsWithoutResourcesErrorComponent
        | ApiV1DatasourcesRescanNotesCreateCreateMaintenanceAsDraftErrorComponent
        | ApiV1DatasourcesRescanNotesCreateCreateNotesResolvedErrorComponent
        | ApiV1DatasourcesRescanNotesCreateCriticalityErrorComponent
        | ApiV1DatasourcesRescanNotesCreateDatasourceUrlErrorComponent
        | ApiV1DatasourcesRescanNotesCreateDebugModeErrorComponent
        | ApiV1DatasourcesRescanNotesCreateDisplayNameErrorComponent
        | ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponent
        | ApiV1DatasourcesRescanNotesCreateKindErrorComponent
        | ApiV1DatasourcesRescanNotesCreateLabelsErrorComponent
        | ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponent
        | ApiV1DatasourcesRescanNotesCreateLastSyncErrorErrorComponent
        | ApiV1DatasourcesRescanNotesCreateNameErrorComponent
        | ApiV1DatasourcesRescanNotesCreateNonFieldErrorsErrorComponent
        | ApiV1DatasourcesRescanNotesCreateNoteKindErrorComponent
        | ApiV1DatasourcesRescanNotesCreateNoteOrganizationIdErrorComponent
        | ApiV1DatasourcesRescanNotesCreateNoteWorkspaceIdErrorComponent
        | ApiV1DatasourcesRescanNotesCreatePlatformServiceErrorComponent
        | ApiV1DatasourcesRescanNotesCreateProviderEntityIdErrorComponent
        | ApiV1DatasourcesRescanNotesCreateProviderErrorComponent
        | ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponent
        | ApiV1DatasourcesRescanNotesCreateProviderReferenceErrorComponent
        | ApiV1DatasourcesRescanNotesCreateReconciliationEnabledErrorComponent
        | ApiV1DatasourcesRescanNotesCreateSlaAvailabilityErrorComponent
        | ApiV1DatasourcesRescanNotesCreateSlaTargetErrorComponent
        | ApiV1DatasourcesRescanNotesCreateSloAvailabilityErrorComponent
        | ApiV1DatasourcesRescanNotesCreateSloTargetErrorComponent
        | ApiV1DatasourcesRescanNotesCreateSyncIntervalMinutesErrorComponent
        | ApiV1DatasourcesRescanNotesCreateTargetAvailabilityErrorComponent
        | ApiV1DatasourcesRescanNotesCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_datasources_rescan_notes_create_annotations_error_component import (
            ApiV1DatasourcesRescanNotesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_archived_at_error_component import (
            ApiV1DatasourcesRescanNotesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_archived_error_component import (
            ApiV1DatasourcesRescanNotesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_archived_reason_error_component import (
            ApiV1DatasourcesRescanNotesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_create_incidents_error_component import (
            ApiV1DatasourcesRescanNotesCreateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesRescanNotesCreateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesRescanNotesCreateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_create_notes_resolved_error_component import (
            ApiV1DatasourcesRescanNotesCreateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_criticality_error_component import (
            ApiV1DatasourcesRescanNotesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_datasource_url_error_component import (
            ApiV1DatasourcesRescanNotesCreateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_debug_mode_error_component import (
            ApiV1DatasourcesRescanNotesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_display_name_error_component import (
            ApiV1DatasourcesRescanNotesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_is_enabled_error_component import (
            ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_kind_error_component import (
            ApiV1DatasourcesRescanNotesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_labels_error_component import (
            ApiV1DatasourcesRescanNotesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_last_sync_error_component import (
            ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_last_sync_error_error_component import (
            ApiV1DatasourcesRescanNotesCreateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_name_error_component import (
            ApiV1DatasourcesRescanNotesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_non_field_errors_error_component import (
            ApiV1DatasourcesRescanNotesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_note_kind_error_component import (
            ApiV1DatasourcesRescanNotesCreateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_note_organization_id_error_component import (
            ApiV1DatasourcesRescanNotesCreateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_note_workspace_id_error_component import (
            ApiV1DatasourcesRescanNotesCreateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_platform_service_error_component import (
            ApiV1DatasourcesRescanNotesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_provider_error_component import (
            ApiV1DatasourcesRescanNotesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_provider_id_error_component import (
            ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_provider_reference_error_component import (
            ApiV1DatasourcesRescanNotesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_reconciliation_enabled_error_component import (
            ApiV1DatasourcesRescanNotesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_sla_availability_error_component import (
            ApiV1DatasourcesRescanNotesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_sla_target_error_component import (
            ApiV1DatasourcesRescanNotesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_slo_availability_error_component import (
            ApiV1DatasourcesRescanNotesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_slo_target_error_component import (
            ApiV1DatasourcesRescanNotesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_sync_interval_minutes_error_component import (
            ApiV1DatasourcesRescanNotesCreateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_target_availability_error_component import (
            ApiV1DatasourcesRescanNotesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_tolerations_error_component import (
            ApiV1DatasourcesRescanNotesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateDatasourceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateSyncIntervalMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateNoteKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateNoteOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateNoteWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateCreateNotesResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateCreateMaintenanceAsDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateCreateIncidentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DatasourcesRescanNotesCreateCreateIncidentsWithoutResourcesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesRescanNotesCreateLastSyncErrorErrorComponent):
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
        from ..models.api_v1_datasources_rescan_notes_create_annotations_error_component import (
            ApiV1DatasourcesRescanNotesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_archived_at_error_component import (
            ApiV1DatasourcesRescanNotesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_archived_error_component import (
            ApiV1DatasourcesRescanNotesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_archived_reason_error_component import (
            ApiV1DatasourcesRescanNotesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_create_incidents_error_component import (
            ApiV1DatasourcesRescanNotesCreateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesRescanNotesCreateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesRescanNotesCreateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_create_notes_resolved_error_component import (
            ApiV1DatasourcesRescanNotesCreateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_criticality_error_component import (
            ApiV1DatasourcesRescanNotesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_datasource_url_error_component import (
            ApiV1DatasourcesRescanNotesCreateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_debug_mode_error_component import (
            ApiV1DatasourcesRescanNotesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_display_name_error_component import (
            ApiV1DatasourcesRescanNotesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_is_enabled_error_component import (
            ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_kind_error_component import (
            ApiV1DatasourcesRescanNotesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_labels_error_component import (
            ApiV1DatasourcesRescanNotesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_last_sync_error_component import (
            ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_last_sync_error_error_component import (
            ApiV1DatasourcesRescanNotesCreateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_name_error_component import (
            ApiV1DatasourcesRescanNotesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_non_field_errors_error_component import (
            ApiV1DatasourcesRescanNotesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_note_kind_error_component import (
            ApiV1DatasourcesRescanNotesCreateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_note_organization_id_error_component import (
            ApiV1DatasourcesRescanNotesCreateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_note_workspace_id_error_component import (
            ApiV1DatasourcesRescanNotesCreateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_platform_service_error_component import (
            ApiV1DatasourcesRescanNotesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_provider_entity_id_error_component import (
            ApiV1DatasourcesRescanNotesCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_provider_error_component import (
            ApiV1DatasourcesRescanNotesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_provider_id_error_component import (
            ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_provider_reference_error_component import (
            ApiV1DatasourcesRescanNotesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_reconciliation_enabled_error_component import (
            ApiV1DatasourcesRescanNotesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_sla_availability_error_component import (
            ApiV1DatasourcesRescanNotesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_sla_target_error_component import (
            ApiV1DatasourcesRescanNotesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_slo_availability_error_component import (
            ApiV1DatasourcesRescanNotesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_slo_target_error_component import (
            ApiV1DatasourcesRescanNotesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_sync_interval_minutes_error_component import (
            ApiV1DatasourcesRescanNotesCreateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_target_availability_error_component import (
            ApiV1DatasourcesRescanNotesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_rescan_notes_create_tolerations_error_component import (
            ApiV1DatasourcesRescanNotesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DatasourcesRescanNotesCreateAnnotationsErrorComponent
                | ApiV1DatasourcesRescanNotesCreateArchivedAtErrorComponent
                | ApiV1DatasourcesRescanNotesCreateArchivedErrorComponent
                | ApiV1DatasourcesRescanNotesCreateArchivedReasonErrorComponent
                | ApiV1DatasourcesRescanNotesCreateCreateIncidentsErrorComponent
                | ApiV1DatasourcesRescanNotesCreateCreateIncidentsWithoutResourcesErrorComponent
                | ApiV1DatasourcesRescanNotesCreateCreateMaintenanceAsDraftErrorComponent
                | ApiV1DatasourcesRescanNotesCreateCreateNotesResolvedErrorComponent
                | ApiV1DatasourcesRescanNotesCreateCriticalityErrorComponent
                | ApiV1DatasourcesRescanNotesCreateDatasourceUrlErrorComponent
                | ApiV1DatasourcesRescanNotesCreateDebugModeErrorComponent
                | ApiV1DatasourcesRescanNotesCreateDisplayNameErrorComponent
                | ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponent
                | ApiV1DatasourcesRescanNotesCreateKindErrorComponent
                | ApiV1DatasourcesRescanNotesCreateLabelsErrorComponent
                | ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponent
                | ApiV1DatasourcesRescanNotesCreateLastSyncErrorErrorComponent
                | ApiV1DatasourcesRescanNotesCreateNameErrorComponent
                | ApiV1DatasourcesRescanNotesCreateNonFieldErrorsErrorComponent
                | ApiV1DatasourcesRescanNotesCreateNoteKindErrorComponent
                | ApiV1DatasourcesRescanNotesCreateNoteOrganizationIdErrorComponent
                | ApiV1DatasourcesRescanNotesCreateNoteWorkspaceIdErrorComponent
                | ApiV1DatasourcesRescanNotesCreatePlatformServiceErrorComponent
                | ApiV1DatasourcesRescanNotesCreateProviderEntityIdErrorComponent
                | ApiV1DatasourcesRescanNotesCreateProviderErrorComponent
                | ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponent
                | ApiV1DatasourcesRescanNotesCreateProviderReferenceErrorComponent
                | ApiV1DatasourcesRescanNotesCreateReconciliationEnabledErrorComponent
                | ApiV1DatasourcesRescanNotesCreateSlaAvailabilityErrorComponent
                | ApiV1DatasourcesRescanNotesCreateSlaTargetErrorComponent
                | ApiV1DatasourcesRescanNotesCreateSloAvailabilityErrorComponent
                | ApiV1DatasourcesRescanNotesCreateSloTargetErrorComponent
                | ApiV1DatasourcesRescanNotesCreateSyncIntervalMinutesErrorComponent
                | ApiV1DatasourcesRescanNotesCreateTargetAvailabilityErrorComponent
                | ApiV1DatasourcesRescanNotesCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_0 = (
                        ApiV1DatasourcesRescanNotesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_1 = (
                        ApiV1DatasourcesRescanNotesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_2 = (
                        ApiV1DatasourcesRescanNotesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_3 = (
                        ApiV1DatasourcesRescanNotesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_4 = (
                        ApiV1DatasourcesRescanNotesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_5 = (
                        ApiV1DatasourcesRescanNotesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_6 = (
                        ApiV1DatasourcesRescanNotesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_7 = (
                        ApiV1DatasourcesRescanNotesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_8 = (
                        ApiV1DatasourcesRescanNotesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_9 = (
                        ApiV1DatasourcesRescanNotesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_10 = (
                        ApiV1DatasourcesRescanNotesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_11 = (
                        ApiV1DatasourcesRescanNotesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_12 = (
                        ApiV1DatasourcesRescanNotesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_13 = (
                        ApiV1DatasourcesRescanNotesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_14 = (
                        ApiV1DatasourcesRescanNotesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_15 = (
                        ApiV1DatasourcesRescanNotesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_16 = (
                        ApiV1DatasourcesRescanNotesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_17 = (
                        ApiV1DatasourcesRescanNotesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_18 = (
                        ApiV1DatasourcesRescanNotesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_19 = (
                        ApiV1DatasourcesRescanNotesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_20 = (
                        ApiV1DatasourcesRescanNotesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_21 = (
                        ApiV1DatasourcesRescanNotesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_22 = (
                        ApiV1DatasourcesRescanNotesCreateDatasourceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_23 = (
                        ApiV1DatasourcesRescanNotesCreateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_24 = (
                        ApiV1DatasourcesRescanNotesCreateSyncIntervalMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_25 = (
                        ApiV1DatasourcesRescanNotesCreateNoteKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_26 = (
                        ApiV1DatasourcesRescanNotesCreateNoteOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_27 = (
                        ApiV1DatasourcesRescanNotesCreateNoteWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_28 = (
                        ApiV1DatasourcesRescanNotesCreateCreateNotesResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_29 = (
                        ApiV1DatasourcesRescanNotesCreateCreateMaintenanceAsDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_30 = (
                        ApiV1DatasourcesRescanNotesCreateCreateIncidentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_31 = (
                        ApiV1DatasourcesRescanNotesCreateCreateIncidentsWithoutResourcesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_32 = (
                        ApiV1DatasourcesRescanNotesCreateLastSyncErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_rescan_notes_create_error_type_33 = (
                        ApiV1DatasourcesRescanNotesCreateLastSyncErrorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_datasources_rescan_notes_create_error_type_34 = (
                    ApiV1DatasourcesRescanNotesCreateProviderEntityIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_datasources_rescan_notes_create_error_type_34

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_datasources_rescan_notes_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_datasources_rescan_notes_create_validation_error.additional_properties = d
        return api_v1_datasources_rescan_notes_create_validation_error

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
