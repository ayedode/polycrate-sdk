from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_policies_update_annotations_error_component import ApiV1PoliciesUpdateAnnotationsErrorComponent
    from ..models.api_v1_policies_update_archived_at_error_component import ApiV1PoliciesUpdateArchivedAtErrorComponent
    from ..models.api_v1_policies_update_archived_error_component import ApiV1PoliciesUpdateArchivedErrorComponent
    from ..models.api_v1_policies_update_archived_reason_error_component import (
        ApiV1PoliciesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_policies_update_criticality_error_component import ApiV1PoliciesUpdateCriticalityErrorComponent
    from ..models.api_v1_policies_update_debug_mode_error_component import ApiV1PoliciesUpdateDebugModeErrorComponent
    from ..models.api_v1_policies_update_description_error_component import ApiV1PoliciesUpdateDescriptionErrorComponent
    from ..models.api_v1_policies_update_display_name_error_component import (
        ApiV1PoliciesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_policies_update_expression_error_component import ApiV1PoliciesUpdateExpressionErrorComponent
    from ..models.api_v1_policies_update_kind_error_component import ApiV1PoliciesUpdateKindErrorComponent
    from ..models.api_v1_policies_update_kinds_selector_error_component import (
        ApiV1PoliciesUpdateKindsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_update_labels_error_component import ApiV1PoliciesUpdateLabelsErrorComponent
    from ..models.api_v1_policies_update_metadata_error_component import ApiV1PoliciesUpdateMetadataErrorComponent
    from ..models.api_v1_policies_update_models_selector_error_component import (
        ApiV1PoliciesUpdateModelsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_update_name_error_component import ApiV1PoliciesUpdateNameErrorComponent
    from ..models.api_v1_policies_update_non_field_errors_error_component import (
        ApiV1PoliciesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_policies_update_order_error_component import ApiV1PoliciesUpdateOrderErrorComponent
    from ..models.api_v1_policies_update_organizations_selector_error_component import (
        ApiV1PoliciesUpdateOrganizationsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_update_platform_service_error_component import (
        ApiV1PoliciesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_policies_update_provider_error_component import ApiV1PoliciesUpdateProviderErrorComponent
    from ..models.api_v1_policies_update_provider_id_error_component import ApiV1PoliciesUpdateProviderIdErrorComponent
    from ..models.api_v1_policies_update_provider_reference_error_component import (
        ApiV1PoliciesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_policies_update_reconciliation_enabled_error_component import (
        ApiV1PoliciesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_policies_update_sla_availability_error_component import (
        ApiV1PoliciesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_update_sla_target_error_component import ApiV1PoliciesUpdateSlaTargetErrorComponent
    from ..models.api_v1_policies_update_slo_availability_error_component import (
        ApiV1PoliciesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_update_slo_target_error_component import ApiV1PoliciesUpdateSloTargetErrorComponent
    from ..models.api_v1_policies_update_target_availability_error_component import (
        ApiV1PoliciesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_update_tolerations_error_component import ApiV1PoliciesUpdateTolerationsErrorComponent
    from ..models.api_v1_policies_update_workspaces_selector_error_component import (
        ApiV1PoliciesUpdateWorkspacesSelectorErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PoliciesUpdateValidationError")


@_attrs_define
class ApiV1PoliciesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PoliciesUpdateAnnotationsErrorComponent | ApiV1PoliciesUpdateArchivedAtErrorComponent |
            ApiV1PoliciesUpdateArchivedErrorComponent | ApiV1PoliciesUpdateArchivedReasonErrorComponent |
            ApiV1PoliciesUpdateCriticalityErrorComponent | ApiV1PoliciesUpdateDebugModeErrorComponent |
            ApiV1PoliciesUpdateDescriptionErrorComponent | ApiV1PoliciesUpdateDisplayNameErrorComponent |
            ApiV1PoliciesUpdateExpressionErrorComponent | ApiV1PoliciesUpdateKindErrorComponent |
            ApiV1PoliciesUpdateKindsSelectorErrorComponent | ApiV1PoliciesUpdateLabelsErrorComponent |
            ApiV1PoliciesUpdateMetadataErrorComponent | ApiV1PoliciesUpdateModelsSelectorErrorComponent |
            ApiV1PoliciesUpdateNameErrorComponent | ApiV1PoliciesUpdateNonFieldErrorsErrorComponent |
            ApiV1PoliciesUpdateOrderErrorComponent | ApiV1PoliciesUpdateOrganizationsSelectorErrorComponent |
            ApiV1PoliciesUpdatePlatformServiceErrorComponent | ApiV1PoliciesUpdateProviderErrorComponent |
            ApiV1PoliciesUpdateProviderIdErrorComponent | ApiV1PoliciesUpdateProviderReferenceErrorComponent |
            ApiV1PoliciesUpdateReconciliationEnabledErrorComponent | ApiV1PoliciesUpdateSlaAvailabilityErrorComponent |
            ApiV1PoliciesUpdateSlaTargetErrorComponent | ApiV1PoliciesUpdateSloAvailabilityErrorComponent |
            ApiV1PoliciesUpdateSloTargetErrorComponent | ApiV1PoliciesUpdateTargetAvailabilityErrorComponent |
            ApiV1PoliciesUpdateTolerationsErrorComponent | ApiV1PoliciesUpdateWorkspacesSelectorErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PoliciesUpdateAnnotationsErrorComponent
        | ApiV1PoliciesUpdateArchivedAtErrorComponent
        | ApiV1PoliciesUpdateArchivedErrorComponent
        | ApiV1PoliciesUpdateArchivedReasonErrorComponent
        | ApiV1PoliciesUpdateCriticalityErrorComponent
        | ApiV1PoliciesUpdateDebugModeErrorComponent
        | ApiV1PoliciesUpdateDescriptionErrorComponent
        | ApiV1PoliciesUpdateDisplayNameErrorComponent
        | ApiV1PoliciesUpdateExpressionErrorComponent
        | ApiV1PoliciesUpdateKindErrorComponent
        | ApiV1PoliciesUpdateKindsSelectorErrorComponent
        | ApiV1PoliciesUpdateLabelsErrorComponent
        | ApiV1PoliciesUpdateMetadataErrorComponent
        | ApiV1PoliciesUpdateModelsSelectorErrorComponent
        | ApiV1PoliciesUpdateNameErrorComponent
        | ApiV1PoliciesUpdateNonFieldErrorsErrorComponent
        | ApiV1PoliciesUpdateOrderErrorComponent
        | ApiV1PoliciesUpdateOrganizationsSelectorErrorComponent
        | ApiV1PoliciesUpdatePlatformServiceErrorComponent
        | ApiV1PoliciesUpdateProviderErrorComponent
        | ApiV1PoliciesUpdateProviderIdErrorComponent
        | ApiV1PoliciesUpdateProviderReferenceErrorComponent
        | ApiV1PoliciesUpdateReconciliationEnabledErrorComponent
        | ApiV1PoliciesUpdateSlaAvailabilityErrorComponent
        | ApiV1PoliciesUpdateSlaTargetErrorComponent
        | ApiV1PoliciesUpdateSloAvailabilityErrorComponent
        | ApiV1PoliciesUpdateSloTargetErrorComponent
        | ApiV1PoliciesUpdateTargetAvailabilityErrorComponent
        | ApiV1PoliciesUpdateTolerationsErrorComponent
        | ApiV1PoliciesUpdateWorkspacesSelectorErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_policies_update_annotations_error_component import (
            ApiV1PoliciesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_archived_at_error_component import (
            ApiV1PoliciesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_archived_error_component import (
            ApiV1PoliciesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_archived_reason_error_component import (
            ApiV1PoliciesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_criticality_error_component import (
            ApiV1PoliciesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_debug_mode_error_component import (
            ApiV1PoliciesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_description_error_component import (
            ApiV1PoliciesUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_display_name_error_component import (
            ApiV1PoliciesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_expression_error_component import (
            ApiV1PoliciesUpdateExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_kind_error_component import (
            ApiV1PoliciesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_kinds_selector_error_component import (
            ApiV1PoliciesUpdateKindsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_labels_error_component import (
            ApiV1PoliciesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_models_selector_error_component import (
            ApiV1PoliciesUpdateModelsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_name_error_component import (
            ApiV1PoliciesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_non_field_errors_error_component import (
            ApiV1PoliciesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_order_error_component import (
            ApiV1PoliciesUpdateOrderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_organizations_selector_error_component import (
            ApiV1PoliciesUpdateOrganizationsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_platform_service_error_component import (
            ApiV1PoliciesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_provider_error_component import (
            ApiV1PoliciesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_provider_id_error_component import (
            ApiV1PoliciesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_provider_reference_error_component import (
            ApiV1PoliciesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_reconciliation_enabled_error_component import (
            ApiV1PoliciesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_sla_availability_error_component import (
            ApiV1PoliciesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_sla_target_error_component import (
            ApiV1PoliciesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_slo_availability_error_component import (
            ApiV1PoliciesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_slo_target_error_component import (
            ApiV1PoliciesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_target_availability_error_component import (
            ApiV1PoliciesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_tolerations_error_component import (
            ApiV1PoliciesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_workspaces_selector_error_component import (
            ApiV1PoliciesUpdateWorkspacesSelectorErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PoliciesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateModelsSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateOrganizationsSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateWorkspacesSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesUpdateKindsSelectorErrorComponent):
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
        from ..models.api_v1_policies_update_annotations_error_component import (
            ApiV1PoliciesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_archived_at_error_component import (
            ApiV1PoliciesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_archived_error_component import (
            ApiV1PoliciesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_archived_reason_error_component import (
            ApiV1PoliciesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_criticality_error_component import (
            ApiV1PoliciesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_debug_mode_error_component import (
            ApiV1PoliciesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_description_error_component import (
            ApiV1PoliciesUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_display_name_error_component import (
            ApiV1PoliciesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_expression_error_component import (
            ApiV1PoliciesUpdateExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_kind_error_component import (
            ApiV1PoliciesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_kinds_selector_error_component import (
            ApiV1PoliciesUpdateKindsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_labels_error_component import (
            ApiV1PoliciesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_metadata_error_component import (
            ApiV1PoliciesUpdateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_models_selector_error_component import (
            ApiV1PoliciesUpdateModelsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_name_error_component import (
            ApiV1PoliciesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_non_field_errors_error_component import (
            ApiV1PoliciesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_order_error_component import (
            ApiV1PoliciesUpdateOrderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_organizations_selector_error_component import (
            ApiV1PoliciesUpdateOrganizationsSelectorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_platform_service_error_component import (
            ApiV1PoliciesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_provider_error_component import (
            ApiV1PoliciesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_provider_id_error_component import (
            ApiV1PoliciesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_provider_reference_error_component import (
            ApiV1PoliciesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_reconciliation_enabled_error_component import (
            ApiV1PoliciesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_sla_availability_error_component import (
            ApiV1PoliciesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_sla_target_error_component import (
            ApiV1PoliciesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_slo_availability_error_component import (
            ApiV1PoliciesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_slo_target_error_component import (
            ApiV1PoliciesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_target_availability_error_component import (
            ApiV1PoliciesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_tolerations_error_component import (
            ApiV1PoliciesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_policies_update_workspaces_selector_error_component import (
            ApiV1PoliciesUpdateWorkspacesSelectorErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PoliciesUpdateAnnotationsErrorComponent
                | ApiV1PoliciesUpdateArchivedAtErrorComponent
                | ApiV1PoliciesUpdateArchivedErrorComponent
                | ApiV1PoliciesUpdateArchivedReasonErrorComponent
                | ApiV1PoliciesUpdateCriticalityErrorComponent
                | ApiV1PoliciesUpdateDebugModeErrorComponent
                | ApiV1PoliciesUpdateDescriptionErrorComponent
                | ApiV1PoliciesUpdateDisplayNameErrorComponent
                | ApiV1PoliciesUpdateExpressionErrorComponent
                | ApiV1PoliciesUpdateKindErrorComponent
                | ApiV1PoliciesUpdateKindsSelectorErrorComponent
                | ApiV1PoliciesUpdateLabelsErrorComponent
                | ApiV1PoliciesUpdateMetadataErrorComponent
                | ApiV1PoliciesUpdateModelsSelectorErrorComponent
                | ApiV1PoliciesUpdateNameErrorComponent
                | ApiV1PoliciesUpdateNonFieldErrorsErrorComponent
                | ApiV1PoliciesUpdateOrderErrorComponent
                | ApiV1PoliciesUpdateOrganizationsSelectorErrorComponent
                | ApiV1PoliciesUpdatePlatformServiceErrorComponent
                | ApiV1PoliciesUpdateProviderErrorComponent
                | ApiV1PoliciesUpdateProviderIdErrorComponent
                | ApiV1PoliciesUpdateProviderReferenceErrorComponent
                | ApiV1PoliciesUpdateReconciliationEnabledErrorComponent
                | ApiV1PoliciesUpdateSlaAvailabilityErrorComponent
                | ApiV1PoliciesUpdateSlaTargetErrorComponent
                | ApiV1PoliciesUpdateSloAvailabilityErrorComponent
                | ApiV1PoliciesUpdateSloTargetErrorComponent
                | ApiV1PoliciesUpdateTargetAvailabilityErrorComponent
                | ApiV1PoliciesUpdateTolerationsErrorComponent
                | ApiV1PoliciesUpdateWorkspacesSelectorErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_0 = (
                        ApiV1PoliciesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_1 = (
                        ApiV1PoliciesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_2 = (
                        ApiV1PoliciesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_3 = (
                        ApiV1PoliciesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_4 = (
                        ApiV1PoliciesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_5 = (
                        ApiV1PoliciesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_6 = (
                        ApiV1PoliciesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_7 = (
                        ApiV1PoliciesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_8 = (
                        ApiV1PoliciesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_9 = (
                        ApiV1PoliciesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_10 = (
                        ApiV1PoliciesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_11 = (
                        ApiV1PoliciesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_12 = (
                        ApiV1PoliciesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_13 = (
                        ApiV1PoliciesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_14 = (
                        ApiV1PoliciesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_15 = (
                        ApiV1PoliciesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_16 = (
                        ApiV1PoliciesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_17 = (
                        ApiV1PoliciesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_18 = (
                        ApiV1PoliciesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_19 = (
                        ApiV1PoliciesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_20 = (
                        ApiV1PoliciesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_21 = (
                        ApiV1PoliciesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_22 = (
                        ApiV1PoliciesUpdateExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_23 = (
                        ApiV1PoliciesUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_24 = (
                        ApiV1PoliciesUpdateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_25 = (
                        ApiV1PoliciesUpdateModelsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_26 = (
                        ApiV1PoliciesUpdateOrganizationsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_27 = (
                        ApiV1PoliciesUpdateWorkspacesSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_update_error_type_28 = (
                        ApiV1PoliciesUpdateKindsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_policies_update_error_type_29 = (
                    ApiV1PoliciesUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_policies_update_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_policies_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_policies_update_validation_error.additional_properties = d
        return api_v1_policies_update_validation_error

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
