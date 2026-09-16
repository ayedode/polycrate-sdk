from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alertrouters_partial_update_annotations_error_component import (
        ApiV1AlertroutersPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_archived_at_error_component import (
        ApiV1AlertroutersPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_archived_error_component import (
        ApiV1AlertroutersPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_archived_reason_error_component import (
        ApiV1AlertroutersPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_criticality_error_component import (
        ApiV1AlertroutersPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_debug_mode_error_component import (
        ApiV1AlertroutersPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_display_name_error_component import (
        ApiV1AlertroutersPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_kind_error_component import (
        ApiV1AlertroutersPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_label_cluster_error_component import (
        ApiV1AlertroutersPartialUpdateLabelClusterErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_label_criticality_error_component import (
        ApiV1AlertroutersPartialUpdateLabelCriticalityErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_label_namespace_error_component import (
        ApiV1AlertroutersPartialUpdateLabelNamespaceErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_label_organization_error_component import (
        ApiV1AlertroutersPartialUpdateLabelOrganizationErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_label_pod_error_component import (
        ApiV1AlertroutersPartialUpdateLabelPodErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_label_workspace_error_component import (
        ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_labels_error_component import (
        ApiV1AlertroutersPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_name_error_component import (
        ApiV1AlertroutersPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_non_field_errors_error_component import (
        ApiV1AlertroutersPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_organization_id_error_component import (
        ApiV1AlertroutersPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_platform_service_error_component import (
        ApiV1AlertroutersPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_provider_error_component import (
        ApiV1AlertroutersPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_provider_id_error_component import (
        ApiV1AlertroutersPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_provider_reference_error_component import (
        ApiV1AlertroutersPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_reconciliation_enabled_error_component import (
        ApiV1AlertroutersPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_sla_availability_error_component import (
        ApiV1AlertroutersPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_sla_target_error_component import (
        ApiV1AlertroutersPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_slo_availability_error_component import (
        ApiV1AlertroutersPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_slo_target_error_component import (
        ApiV1AlertroutersPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_target_availability_error_component import (
        ApiV1AlertroutersPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_tolerations_error_component import (
        ApiV1AlertroutersPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_alertrouters_partial_update_workspace_id_error_component import (
        ApiV1AlertroutersPartialUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertroutersPartialUpdateValidationError")


@_attrs_define
class ApiV1AlertroutersPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertroutersPartialUpdateAnnotationsErrorComponent |
            ApiV1AlertroutersPartialUpdateArchivedAtErrorComponent | ApiV1AlertroutersPartialUpdateArchivedErrorComponent |
            ApiV1AlertroutersPartialUpdateArchivedReasonErrorComponent |
            ApiV1AlertroutersPartialUpdateCriticalityErrorComponent | ApiV1AlertroutersPartialUpdateDebugModeErrorComponent
            | ApiV1AlertroutersPartialUpdateDisplayNameErrorComponent | ApiV1AlertroutersPartialUpdateKindErrorComponent |
            ApiV1AlertroutersPartialUpdateLabelClusterErrorComponent |
            ApiV1AlertroutersPartialUpdateLabelCriticalityErrorComponent |
            ApiV1AlertroutersPartialUpdateLabelNamespaceErrorComponent |
            ApiV1AlertroutersPartialUpdateLabelOrganizationErrorComponent |
            ApiV1AlertroutersPartialUpdateLabelPodErrorComponent | ApiV1AlertroutersPartialUpdateLabelsErrorComponent |
            ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponent | ApiV1AlertroutersPartialUpdateNameErrorComponent |
            ApiV1AlertroutersPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1AlertroutersPartialUpdateOrganizationIdErrorComponent |
            ApiV1AlertroutersPartialUpdatePlatformServiceErrorComponent |
            ApiV1AlertroutersPartialUpdateProviderErrorComponent | ApiV1AlertroutersPartialUpdateProviderIdErrorComponent |
            ApiV1AlertroutersPartialUpdateProviderReferenceErrorComponent |
            ApiV1AlertroutersPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1AlertroutersPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1AlertroutersPartialUpdateSlaTargetErrorComponent |
            ApiV1AlertroutersPartialUpdateSloAvailabilityErrorComponent |
            ApiV1AlertroutersPartialUpdateSloTargetErrorComponent |
            ApiV1AlertroutersPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1AlertroutersPartialUpdateTolerationsErrorComponent |
            ApiV1AlertroutersPartialUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertroutersPartialUpdateAnnotationsErrorComponent
        | ApiV1AlertroutersPartialUpdateArchivedAtErrorComponent
        | ApiV1AlertroutersPartialUpdateArchivedErrorComponent
        | ApiV1AlertroutersPartialUpdateArchivedReasonErrorComponent
        | ApiV1AlertroutersPartialUpdateCriticalityErrorComponent
        | ApiV1AlertroutersPartialUpdateDebugModeErrorComponent
        | ApiV1AlertroutersPartialUpdateDisplayNameErrorComponent
        | ApiV1AlertroutersPartialUpdateKindErrorComponent
        | ApiV1AlertroutersPartialUpdateLabelClusterErrorComponent
        | ApiV1AlertroutersPartialUpdateLabelCriticalityErrorComponent
        | ApiV1AlertroutersPartialUpdateLabelNamespaceErrorComponent
        | ApiV1AlertroutersPartialUpdateLabelOrganizationErrorComponent
        | ApiV1AlertroutersPartialUpdateLabelPodErrorComponent
        | ApiV1AlertroutersPartialUpdateLabelsErrorComponent
        | ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponent
        | ApiV1AlertroutersPartialUpdateNameErrorComponent
        | ApiV1AlertroutersPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1AlertroutersPartialUpdateOrganizationIdErrorComponent
        | ApiV1AlertroutersPartialUpdatePlatformServiceErrorComponent
        | ApiV1AlertroutersPartialUpdateProviderErrorComponent
        | ApiV1AlertroutersPartialUpdateProviderIdErrorComponent
        | ApiV1AlertroutersPartialUpdateProviderReferenceErrorComponent
        | ApiV1AlertroutersPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1AlertroutersPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1AlertroutersPartialUpdateSlaTargetErrorComponent
        | ApiV1AlertroutersPartialUpdateSloAvailabilityErrorComponent
        | ApiV1AlertroutersPartialUpdateSloTargetErrorComponent
        | ApiV1AlertroutersPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1AlertroutersPartialUpdateTolerationsErrorComponent
        | ApiV1AlertroutersPartialUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alertrouters_partial_update_annotations_error_component import (
            ApiV1AlertroutersPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_archived_at_error_component import (
            ApiV1AlertroutersPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_archived_error_component import (
            ApiV1AlertroutersPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_archived_reason_error_component import (
            ApiV1AlertroutersPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_criticality_error_component import (
            ApiV1AlertroutersPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_debug_mode_error_component import (
            ApiV1AlertroutersPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_display_name_error_component import (
            ApiV1AlertroutersPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_kind_error_component import (
            ApiV1AlertroutersPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_label_cluster_error_component import (
            ApiV1AlertroutersPartialUpdateLabelClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_label_namespace_error_component import (
            ApiV1AlertroutersPartialUpdateLabelNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_label_organization_error_component import (
            ApiV1AlertroutersPartialUpdateLabelOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_label_pod_error_component import (
            ApiV1AlertroutersPartialUpdateLabelPodErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_label_workspace_error_component import (
            ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_labels_error_component import (
            ApiV1AlertroutersPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_name_error_component import (
            ApiV1AlertroutersPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_non_field_errors_error_component import (
            ApiV1AlertroutersPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_organization_id_error_component import (
            ApiV1AlertroutersPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_platform_service_error_component import (
            ApiV1AlertroutersPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_provider_error_component import (
            ApiV1AlertroutersPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_provider_id_error_component import (
            ApiV1AlertroutersPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_provider_reference_error_component import (
            ApiV1AlertroutersPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_reconciliation_enabled_error_component import (
            ApiV1AlertroutersPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_sla_availability_error_component import (
            ApiV1AlertroutersPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_sla_target_error_component import (
            ApiV1AlertroutersPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_slo_availability_error_component import (
            ApiV1AlertroutersPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_slo_target_error_component import (
            ApiV1AlertroutersPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_target_availability_error_component import (
            ApiV1AlertroutersPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_tolerations_error_component import (
            ApiV1AlertroutersPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_workspace_id_error_component import (
            ApiV1AlertroutersPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateLabelOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateLabelClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateLabelPodErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersPartialUpdateLabelNamespaceErrorComponent):
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
        from ..models.api_v1_alertrouters_partial_update_annotations_error_component import (
            ApiV1AlertroutersPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_archived_at_error_component import (
            ApiV1AlertroutersPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_archived_error_component import (
            ApiV1AlertroutersPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_archived_reason_error_component import (
            ApiV1AlertroutersPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_criticality_error_component import (
            ApiV1AlertroutersPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_debug_mode_error_component import (
            ApiV1AlertroutersPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_display_name_error_component import (
            ApiV1AlertroutersPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_kind_error_component import (
            ApiV1AlertroutersPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_label_cluster_error_component import (
            ApiV1AlertroutersPartialUpdateLabelClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_label_criticality_error_component import (
            ApiV1AlertroutersPartialUpdateLabelCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_label_namespace_error_component import (
            ApiV1AlertroutersPartialUpdateLabelNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_label_organization_error_component import (
            ApiV1AlertroutersPartialUpdateLabelOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_label_pod_error_component import (
            ApiV1AlertroutersPartialUpdateLabelPodErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_label_workspace_error_component import (
            ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_labels_error_component import (
            ApiV1AlertroutersPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_name_error_component import (
            ApiV1AlertroutersPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_non_field_errors_error_component import (
            ApiV1AlertroutersPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_organization_id_error_component import (
            ApiV1AlertroutersPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_platform_service_error_component import (
            ApiV1AlertroutersPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_provider_error_component import (
            ApiV1AlertroutersPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_provider_id_error_component import (
            ApiV1AlertroutersPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_provider_reference_error_component import (
            ApiV1AlertroutersPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_reconciliation_enabled_error_component import (
            ApiV1AlertroutersPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_sla_availability_error_component import (
            ApiV1AlertroutersPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_sla_target_error_component import (
            ApiV1AlertroutersPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_slo_availability_error_component import (
            ApiV1AlertroutersPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_slo_target_error_component import (
            ApiV1AlertroutersPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_target_availability_error_component import (
            ApiV1AlertroutersPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_tolerations_error_component import (
            ApiV1AlertroutersPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_alertrouters_partial_update_workspace_id_error_component import (
            ApiV1AlertroutersPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertroutersPartialUpdateAnnotationsErrorComponent
                | ApiV1AlertroutersPartialUpdateArchivedAtErrorComponent
                | ApiV1AlertroutersPartialUpdateArchivedErrorComponent
                | ApiV1AlertroutersPartialUpdateArchivedReasonErrorComponent
                | ApiV1AlertroutersPartialUpdateCriticalityErrorComponent
                | ApiV1AlertroutersPartialUpdateDebugModeErrorComponent
                | ApiV1AlertroutersPartialUpdateDisplayNameErrorComponent
                | ApiV1AlertroutersPartialUpdateKindErrorComponent
                | ApiV1AlertroutersPartialUpdateLabelClusterErrorComponent
                | ApiV1AlertroutersPartialUpdateLabelCriticalityErrorComponent
                | ApiV1AlertroutersPartialUpdateLabelNamespaceErrorComponent
                | ApiV1AlertroutersPartialUpdateLabelOrganizationErrorComponent
                | ApiV1AlertroutersPartialUpdateLabelPodErrorComponent
                | ApiV1AlertroutersPartialUpdateLabelsErrorComponent
                | ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponent
                | ApiV1AlertroutersPartialUpdateNameErrorComponent
                | ApiV1AlertroutersPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1AlertroutersPartialUpdateOrganizationIdErrorComponent
                | ApiV1AlertroutersPartialUpdatePlatformServiceErrorComponent
                | ApiV1AlertroutersPartialUpdateProviderErrorComponent
                | ApiV1AlertroutersPartialUpdateProviderIdErrorComponent
                | ApiV1AlertroutersPartialUpdateProviderReferenceErrorComponent
                | ApiV1AlertroutersPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1AlertroutersPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1AlertroutersPartialUpdateSlaTargetErrorComponent
                | ApiV1AlertroutersPartialUpdateSloAvailabilityErrorComponent
                | ApiV1AlertroutersPartialUpdateSloTargetErrorComponent
                | ApiV1AlertroutersPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1AlertroutersPartialUpdateTolerationsErrorComponent
                | ApiV1AlertroutersPartialUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_0 = (
                        ApiV1AlertroutersPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_1 = (
                        ApiV1AlertroutersPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_2 = (
                        ApiV1AlertroutersPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_3 = (
                        ApiV1AlertroutersPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_4 = (
                        ApiV1AlertroutersPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_5 = (
                        ApiV1AlertroutersPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_6 = (
                        ApiV1AlertroutersPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_7 = (
                        ApiV1AlertroutersPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_8 = (
                        ApiV1AlertroutersPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_9 = (
                        ApiV1AlertroutersPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_10 = (
                        ApiV1AlertroutersPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_11 = (
                        ApiV1AlertroutersPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_12 = (
                        ApiV1AlertroutersPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_13 = (
                        ApiV1AlertroutersPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_14 = (
                        ApiV1AlertroutersPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_15 = (
                        ApiV1AlertroutersPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_16 = (
                        ApiV1AlertroutersPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_17 = (
                        ApiV1AlertroutersPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_18 = (
                        ApiV1AlertroutersPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_19 = (
                        ApiV1AlertroutersPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_20 = (
                        ApiV1AlertroutersPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_21 = (
                        ApiV1AlertroutersPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_22 = (
                        ApiV1AlertroutersPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_23 = (
                        ApiV1AlertroutersPartialUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_24 = (
                        ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_25 = (
                        ApiV1AlertroutersPartialUpdateLabelOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_26 = (
                        ApiV1AlertroutersPartialUpdateLabelClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_27 = (
                        ApiV1AlertroutersPartialUpdateLabelPodErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_partial_update_error_type_28 = (
                        ApiV1AlertroutersPartialUpdateLabelNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alertrouters_partial_update_error_type_29 = (
                    ApiV1AlertroutersPartialUpdateLabelCriticalityErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alertrouters_partial_update_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alertrouters_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alertrouters_partial_update_validation_error.additional_properties = d
        return api_v1_alertrouters_partial_update_validation_error

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
